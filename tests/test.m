#import "test.h"

id doWork() {
    return [Foo p4Default];
}

@implementation Foo

- (NSObject<MyObserver> *)p4Default {
    return nil;
}

- (Foo *)someMethod:(int)i withString:(NSString *)s {
    Foo *foo = [[Foo alloc] initWithP2:42];
    return foo;
}

+ (NSObject<MyObserver> *)p4Default {
    return nil;
}
@end
