#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:44
:Licence GNUv3
Part of lambda-cli

"""

from unittest import TestCase, main
from grammpy_transforms import ContextFree, InverseCommon, InverseContextFree
from pyparsers import cyk
from lambda_cli import lambda_grammar, lambda_cli_lex


class FromAlphaReductionTest(TestCase):
    def setUp(self):
        self.g = lambda_grammar
        self.g = ContextFree.remove_useless_symbols(self.g)
        self.g = ContextFree.remove_rules_with_epsilon(self.g, transform_grammar=True)
        self.g = ContextFree.remove_unit_rules(self.g, transform_grammar=True)
        self.g = ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        self.g = ContextFree.transform_to_chomsky_normal_form(self.g, transform_grammar=True)

    def test_001(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda x y. (x y)) y)"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_002(self):
        parsed = cyk(self.g, lambda_cli_lex("(lambda y'. (y y'))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_003(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda x. (lambda z. (x z))) (z g))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_004(self):
        parsed = cyk(self.g, lambda_cli_lex("(lambda z'. ((z g) z'))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_005(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda y. (lambda z. (z y))) y z)"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_006(self):
        parsed = cyk(self.g, lambda_cli_lex("(z y)"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_007(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda x. (lambda y. (y (lambda x. x) x))) x)"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_008(self):
        parsed = cyk(self.g, lambda_cli_lex("(lambda y. (y (lambda x'. x') x))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()


if __name__ == '__main__':
    main()
