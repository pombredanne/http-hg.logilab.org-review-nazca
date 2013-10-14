# -*- coding:utf-8 -*-
#
# copyright 2012 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

import unittest2
import random
random.seed(6) ### Make sure tests are repeatable
from dateutil import parser as dateparser

from nazca.distances import (levenshtein, soundex, soundexcode,\
                             jaccard, euclidean, geographical,
                             LevenshteinProcessing)


class DistancesTest(unittest2.TestCase):
    def test_levenshtein(self):
        self.assertEqual(levenshtein('niche', 'chiens'), 5)
        self.assertEqual(levenshtein('bonjour', 'bonjour !'), 1)
        self.assertEqual(levenshtein('bon', 'bonjour'), 4)
        self.assertEqual(levenshtein('Victor Hugo', 'Hugo Victor'), 0)

        #Test symetry
        self.assertEqual(levenshtein('Victor Hugo', 'Vitor Wugo'),
                         levenshtein('Vitor Wugo', 'Victor Hugo'))

    def test_soundex(self):
        ##     Test extracted from Wikipedia en :
        #Using this algorithm :
        #both "Robert" and "Rupert" return the same string "R163"
        #while "Rubin" yields "R150".
        #
        # "Ashcraft" and "Ashcroft" both yield "A261" and not "A226"
        #(the chars 's' and 'c' in the name would receive a single number
        #of 2 and not 22 since an 'h' lies in between them).
        #
        # "Tymczak" yields "T522" not "T520"
        #(the chars 'z' and 'k' in the name are coded as 2 twice since a vowel
        #lies in between them).
        #
        #"Pfister" yields "P236" not "P123" (the first two letters have the same
        #number and are coded once as 'P').

        self.assertEqual(soundexcode('Robert', 'english'), 'R163')
        self.assertEqual(soundexcode('Rubert', 'english'), 'R163')
        self.assertEqual(soundexcode('Rubin', 'english'), 'R150')
        self.assertEqual(soundexcode('Ashcraft', 'english'), 'A261')
        self.assertEqual(soundexcode('Tymczak', 'english'), 'T522')
        self.assertEqual(soundexcode('Pfister', 'english'), 'P236')

        self.assertEqual(soundex('Rubert', 'Robert', 'english'), 0)
        self.assertEqual(soundex('Rubin', 'Robert', 'english'), 1)

    def test_jaccard(self):
        #The jaccard indice between two words is the ratio of the number of
        #identical letters and the total number of letters
        #Each letter is counted once only
        #The distance is 1 - jaccard_indice

        self.assertEqual(jaccard('bonjour', 'bonjour'), 0.0)
        self.assertAlmostEqual(jaccard('boujour', 'bonjour'), 1, 2)
        self.assertAlmostEqual(jaccard(u'sacré rubert', u'sacré hubert'), 0.667, 2)

        #Test symetry
        self.assertEqual(jaccard('orange', 'morange'),
                         jaccard('morange', 'orange'))

    def test_temporal(self):
        #Test the distance between two dates. The distance can be given in
        #``days``, ``months`` or ``years``
        try:
            from nazca.distances import temporal
        except ImportError:
            return
        self.assertEqual(temporal('14 aout 1991', '14/08/1991'), 0)
        self.assertEqual(temporal('14 aout 1991', '08/14/1991'), 0)
        self.assertEqual(temporal('14 aout 1991', '08/15/1992'), 367)
        #Test a case of ambiguity
        self.assertEqual(temporal('1er mai 2012', '01/05/2012'), 0)
        self.assertEqual(temporal('1er mai 2012', '05/01/2012', dayfirst=False), 0)
        #Test the different granularities available
        self.assertAlmostEqual(temporal('14 aout 1991', '08/15/1992', 'years'), 1.0, 1)
        self.assertAlmostEqual(temporal('1991', '1992', 'years'), 1.0, 1)
        self.assertAlmostEqual(temporal('13 mars', '13 mai', 'months'), 2.0, 1)
        self.assertAlmostEqual(temporal('13 march', '13 may', 'months',
                                        parserinfo=dateparser.parserinfo), 2.0, 1)

        #Test fuzzyness
        self.assertEqual(temporal('Jean est né le 1er octobre 1958',
                                  'Le 01-10-1958, Jean est né'), 0)

        #Test symetry
        self.assertEqual(temporal('14-08-1991', '15/08/1992'),
                         temporal('15/08/1992', '14/08/1991'))

    def test_euclidean(self):
        self.assertEqual(euclidean(10, 11), 1)
        self.assertEqual(euclidean(-10, 11), 21)
        self.assertEqual(euclidean('-10', '11'), 21)

        #Test symetry
        self.assertEqual(euclidean(10, 11),
                         euclidean(11, 10))

    def test_geographical(self):
        paris = (48.856578, 2.351828)
        london = (51.504872, -0.07857)
        dist_parislondon = geographical(paris, london, in_radians=False)

        self.assertAlmostEqual(dist_parislondon, 341564, 0)


class MatrixTestCase(unittest2.TestCase):

    def setUp(self):
        self.input1 = [u'Victor Hugo', u'Albert Camus', 'Jean Valjean']
        self.input2 = [u'Victor Wugo', u'Albert Camus', 'Albert Camu']
        self.distance = levenshtein
        processing = LevenshteinProcessing()
        self.matrix = processing.cdist(self.input1, self.input2)

    def test_matrixconstruction(self):
        d = self.distance
        i1, i2 = self.input1, self.input2
        m = self.matrix

        for i in xrange(len(i1)):
            for j in xrange(len(i2)):
                self.assertAlmostEqual(m[i, j], d(i1[i], i2[j]), 4)

    def test_operation(self):
        m = self.matrix
        self.assertTrue((3 * m == m * 3).all())
        self.assertTrue(((m - 0.5*m) == (0.5 * m)).all())
        self.assertTrue(((m + 10*m - m * 3) == (8 * m)).all())

    def test_pdist(self):
        _input = [u'Victor Wugo', u'Albert Camus', 'Albert Camu']
        d = self.distance
        processing = LevenshteinProcessing()
        pdist = processing.pdist(_input)
        self.assertEqual([6, 6, 1], pdist)


if __name__ == '__main__':
    unittest2.main()
