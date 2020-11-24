#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Arboles_formulas as Arb

negacion = ['-']
conectivos_bin = ['Y', 'O', '>', '=']


def inorder_to_tree(inorder):
    if len(inorder) == 1:
        return Arb.Tree_f(inorder[0], None, None)
    elif inorder[0] in negacion:
        return Arb.Tree_f(inorder[0], None, inorder_to_tree(inorder[1:]))
    elif inorder[0] == "(":
        counter = 0                     #Contador de parentesis
        for i in range(1, len(inorder)):
            if inorder[i] == "(":
                counter += 1
            elif inorder[i] == ")":
                counter -=1
            elif inorder[i] in conectivos_bin and counter == 0:
                return Arb.Tree_f(inorder[i], inorder_to_tree(inorder[1:i]), inorder_to_tree(inorder[i + 1:-1]))
    else:
        return -1



test = "p"
test2 = "-p"
test3 = "(p=q)"
test4 = "(-p>((pY-q)>-(pYq)))"

Tree = inorder_to_tree(test)
Tree2 = inorder_to_tree(test2)
Tree3 = inorder_to_tree(test3)
Tree4 = inorder_to_tree(test4)

print(Tree.inorder())
print(Tree2.inorder())
print(Tree3.inorder())
print(Tree4.inorder())
