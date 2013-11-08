#!/usr/bin/env python

# Generates C macros that generates the isEqual: and hash methods for an
# Objective-C class.
#
# Author: Stefan Wehr

MACRO_EQUAL_HASH_BASE_NAME = 'MPGenerateIsEqualHash'
MACRO_DESCRIPTION_BASE_NAME = 'MPGenerateDescription'
MACRO_EQUAL_HASH_DESCRIPTION_BASE_NAME = 'MPGenerateIsEqualHashDescription'
MAX_ARGS = 40

def mangle(s):
    return '__%s' % s

OTHER = mangle('other')
OTHER_CAST = mangle('other_cast')
CLASS = mangle('class')
RESULT = mangle('result')

def fieldType(n):
    return mangle('t%d' % n)

def fieldName(n):
    return mangle('f%d' % n)

def boolvar(n):
    return mangle('b%d' % n)

def call(target, m):
    return '[%s %s]' % (target, m)

def codeForEqTestOfField(n):
    return ['if (![%s is:%s equalTo:%s]) return NO;' % \
                (fieldType(n),
                 call('self', fieldName(n)),
                 call(OTHER_CAST, fieldName(n)))]

def codeForHashOfField(n):
    return ['%s = 37 * %s + [%s hashOf:%s];' % \
                (RESULT, RESULT, fieldType(n), call('self', fieldName(n)))]

def codeForDescriptionOfField(n, isLast):
    l = ['[%s appendString:@#%s];' % (RESULT, fieldName(n)),
         '[%s appendString:@"="];' % RESULT,
         '[%s appendString:[%s descriptionOf:%s]];' % \
             (RESULT, fieldType(n), call('self', fieldName(n)))]
    if not isLast:
        l = l + ['[%s appendString:@", "];' % RESULT]
    return l

def codeForIsEqual(n):
    prefix = ['- (BOOL)isEqual:(id)%s {' % OTHER,
              '  if (%s == self) { return YES; }' % OTHER,
              '  if ([%s isMemberOfClass:[self class]]) {' % OTHER,
              '    %s *%s = (%s *)%s;' % (CLASS, OTHER_CAST, CLASS, OTHER)]
    suffix = ['  } else { return NO; }',
              '}']
    vars = []
    tests = []
    for i  in range(0,n):
        vars = vars + indent(4, codeForEqTestOfField(i))
        tests.append(boolvar(i))
    return prefix + vars + ['    return YES;'] + suffix

def codeForHash(n):
    prefix = ['- (NSUInteger)hash {',
              '  NSUInteger %s = 17;' % RESULT]
    stmts = []
    for i in range(0,n):
        stmts = stmts + codeForHashOfField(i)
    suffix = ['  return %s;' % RESULT,
              '}']
    return prefix + indent(2, stmts) + suffix

def codeForDescription(n, useArc):
    prefix = ['- (NSString *)description {',
              '  NSMutableString *%s = [[NSMutableString alloc] init];' %\
                  RESULT,
              '  [%s appendString:NSStringFromClass([self class])];' % RESULT,
              '  [%s appendString:@" { "];' % RESULT];

    if useArc:
        stmts = []
    else:
        stmts = ['[%s autorelease];' % RESULT]
    for i in range(0,n):
        stmts = stmts + codeForDescriptionOfField(i, i == (n-1))
    suffix = ['  [%s appendString:@" }"];' % RESULT,
              '  return %s;' % RESULT,
              '}']
    return prefix + indent(2, stmts) + suffix

def code(n, useArc):
    args = []
    for i in range(0,n):
        args.append(fieldType(i))
        args.append(fieldName(i))
    args = ','.join(args)
    header1 = ['#define %s%d(%s,%s)' % (MACRO_EQUAL_HASH_BASE_NAME, n, CLASS, args)]
    header2 = ['#define %s%d(%s)' % (MACRO_DESCRIPTION_BASE_NAME, n, args)]
    header3 = ['#define %s%d(%s,%s)' % \
                   (MACRO_EQUAL_HASH_DESCRIPTION_BASE_NAME, n, CLASS, args)]
    c1 = indent(2, codeForIsEqual(n)) + indent(2, codeForHash(n))
    c2 = indent(2, codeForDescription(n, useArc))
    c3 = ['  %s%d(%s,%s)' % (MACRO_EQUAL_HASH_BASE_NAME, n, CLASS, args),
          '  %s%d(%s)' % (MACRO_DESCRIPTION_BASE_NAME, n, args)]
    return (flattenCode(header1 + c1) + '\n' + flattenCode(header2 + c2) + '\n' +
            flattenCode(header3 + c3))

def indent(n, l):
    return [n*' ' + x for x in l]

def flattenCode(l):
    return ' \\\n'.join(l)

def gen(useArc):
    for i in range(1, MAX_ARGS+1):
        print code(i, useArc)
        print

if __name__ == '__main__':
    print '#if __has_feature(objc_arc)'
    gen(useArc=True)
    print '#else'
    gen(useArc=False)
    print '#endif'
