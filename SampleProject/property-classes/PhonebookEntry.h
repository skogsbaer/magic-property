#import <Foundation/Foundation.h>

@interface PhonebookEntry : NSObject
@property (nonatomic, strong, readonly) NSString *name;
@property (nonatomic, strong, readonly) NSString *email;
@property (nonatomic, strong, readonly) NSArray *phoneNumbers;
@property (nonatomic, strong, readonly) NSString *birthday;
@end
