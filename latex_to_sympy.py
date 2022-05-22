import sympy as sp
from sympy import *
import sympy.abc
import string
import re
print('α')
unicode_greek_letters = ['Α', 'α',
                         'Β', 'β',
                         'Γ', 'γ',
                         'Δ', 'δ',
                         'Ε', 'ε',
                         'Ζ', 'ζ',
                         'Η', 'η',
                         'Θ', 'θ',
                         'Ι', 'ι',
                         'Κ', 'κ',
                         'Λ', 'λ',
                         'Μ', 'μ',
                         'Ν', 'ν',
                         'Ξ', 'ξ',
                         'Ο', 'ο',
                         'Π', 'π',
                         'Ρ', 'ρ',
                         'Σ', 'σ',
                         'Τ', 'τ',
                         'Υ', 'υ',
                         'Φ', 'φ',
                         'Χ', 'χ',
                         'Ψ', 'ψ',
                         'Ω', 'ω']
latex_greek_letters = ['\\Alpha',
                       '\\alpha',
                       '\\Beta',
                       '\\beta',
                       '\\Gamma',
                       '\\gamma',
                       '\\Delta',
                       '\\delta',
                       '\\Epsilon',
                       '\\epsilon',
                       '\\Zeta',
                       '\\zeta',
                       '\\Eta',
                       '\\eta',
                       '\\Theta',
                       '\\theta',
                       '\\Iota',
                       '\\iota',
                       '\\Kappa',
                       '\\kappa',
                       '\\Lambda',
                       '\\lambda',
                       '\\Mu',
                       '\\mu',
                       '\\Nu',
                       '\\nu',
                       '\\Xi',
                       '\\xi',
                       '\\Omicron',
                       '\\omicron',
                       '\\Pi',
                       '\\pi',
                       '\\Rho',
                       '\\rho',
                       '\\Sigma',
                       '\\sigma',
                       '\\Tau',
                       '\\tau',
                       '\\Upsilon',
                       '\\upsilon',
                       '\\Phi',
                       '\\phi',
                       '\\Chi',
                       '\\chi',
                       '\\Psi',
                       '\\psi',
                       '\\Omega',
                       '\\omega']




with open('text41.tex', 'r', encoding = 'utf-8') as f:
        
    exprs = []
    
    for item in f:
        item = item.replace('$$', '$')
        
        t = re.findall(r'\\begin{equation}(.*?)\\end{equation}', item)
        if len(t)>0:
            for st in t:
                exprs.append(st)
        t = re.findall(r'\$([^$]+=[^$]+)\$', item)
        if len(t)>0:
            for st in t:
                exprs.append(st)
        #    print(len(re.findall(r'\$([^$]+=[^$]+)\$', item)))
            
        
    #print(formulas, '\n')
    
    #print(exprs)
    for j in range(len(exprs)):
        exprs[j] = exprs[j].replace('frac', '') ## replace fraction
        exprs[j] = exprs[j].replace('}{', ')/(')
        exprs[j] = exprs[j].replace('{', '(')
        exprs[j] = exprs[j].replace('}', ')')
        
        exprs[j] = exprs[j].replace('\\', '')
       # for i in range(len(latex_greek_letters)): ##replace greek to unicode
        #    exprs[j] = exprs[j].replace(latex_greek_letters[i], unicode_greek_letters[i])
            
    #    print(exprs[j]) 
    #print(exprs)
    ##convert strings to sympy
    simbol_exprs = []
    for ex in exprs:
        parts = ex.split('=')
        #print(parts)
        if len(parts) == 1:
            simbol_exprs.append(sympify(parts[0]))
        elif len(parts) > 1:
            for i in range(len(parts)-1):
                simbol_exprs.append(Eq(sympify(parts[i]), sympify(parts[i+1])))
    print(simbol_exprs)
