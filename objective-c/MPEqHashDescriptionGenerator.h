//
//  EqHashDescriptionGenerator.h
//  DociPad
//
//  Created by Stefan Wehr on 9.4.10.
//  Copyright factis research GmbH 2010. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface MPObject : NSObject {
}
+ (BOOL)is:(id)o1 equalTo:(id)o2;
+ (NSUInteger)hashOf:(id)o;
+ (NSString *)descriptionOf:(id)o;
@end

@interface MPIdentity : NSObject {
}
+ (BOOL)is:(id)o1 equalTo:(id)o2;
+ (NSUInteger)hashOf:(id)o;
+ (NSString *)descriptionOf:(id)o;
@end

@interface MPData : NSObject {
}
+ (BOOL)is:(NSData *)o1 equalTo:(NSData *)o2;
+ (NSUInteger)hashOf:(NSData *)o;
+ (NSString *)descriptionOf:(NSData *)o;
@end

@interface MPRect : NSObject {
}
+ (BOOL)is:(CGRect)o1 equalTo:(CGRect)o2;
+ (NSUInteger)hashOf:(CGRect)o;
+ (NSString *)descriptionOf:(CGRect)o;
@end

@interface MPSize : NSObject {
}
+ (BOOL)is:(CGSize)o1 equalTo:(CGSize)o2;
+ (NSUInteger)hashOf:(CGSize)o;
+ (NSString *)descriptionOf:(CGSize)o;
@end

@interface MPPoint : NSObject {
}
+ (BOOL)is:(CGPoint)o1 equalTo:(CGPoint)o2;
+ (NSUInteger)hashOf:(CGPoint)o;
+ (NSString *)descriptionOf:(CGPoint)o;
@end

@interface MPString : NSObject {
}
+ (BOOL)is:(NSString *)o1 equalTo:(NSString *)o2;
+ (NSUInteger)hashOf:(NSString *)o;
+ (NSString *)descriptionOf:(NSString *)o;
@end

@interface MPInteger : NSObject {
}
+ (BOOL)is:(NSInteger)i1 equalTo:(NSInteger)i2;
+ (NSUInteger)hashOf:(NSInteger)i;
+ (NSString *)descriptionOf:(NSInteger)i;
@end

@interface MPUInteger : NSObject {
}
+ (BOOL)is:(NSUInteger)i1 equalTo:(NSUInteger)i2;
+ (NSUInteger)hashOf:(NSUInteger)i;
+ (NSString *)descriptionOf:(NSUInteger)i;
@end

@interface MPInteger64 : NSObject {
}
+ (BOOL)is:(int64_t)i1 equalTo:(int64_t)i2;
+ (NSUInteger)hashOf:(int64_t)i;
+ (NSString *)descriptionOf:(int64_t)i;
@end

@interface MPUInteger64 : NSObject {
}
+ (BOOL)is:(uint64_t)i1 equalTo:(uint64_t)i2;
+ (NSUInteger)hashOf:(uint64_t)i;
+ (NSString *)descriptionOf:(uint64_t)i;
@end

@interface MPBool : NSObject {
}
+ (BOOL)is:(BOOL)b1 equalTo:(BOOL)b2;
+ (NSUInteger)hashOf:(BOOL)b;
+ (NSString *)descriptionOf:(BOOL)b;
@end

@interface MPDouble : NSObject {
}
+ (BOOL)is:(double)i1 equalTo:(double)i2;
+ (NSUInteger)hashOf:(double)i;
+ (NSString *)descriptionOf:(double)i;
@end

@interface MPSelector : NSObject {
}
+ (BOOL)is:(SEL)sel1 equalTo:(SEL)sel2;
+ (NSUInteger)hashOf:(SEL)sel;
+ (NSString *)descriptionOf:(SEL)sel;
@end
