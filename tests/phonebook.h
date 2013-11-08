#import <Foundation/Foundation.h>

#import "Address.h"

@interface PhonebookEntry : NSObject
@property (nonatomic, strong, readonly) NSString *name;
@property (nonatomic, strong, readonly) NSString *email;
@property (nonatomic, strong, readonly) NSArray *phoneNumbers;
@property (nonatomic, strong, readonly) NSString *birthday;
@property (nonatomic, strong, readonly) Address *address;
@end
