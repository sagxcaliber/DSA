# # class burger:
# #     onion = "onion"
# #
# #     def __init__(self):
# #         self.bun = 'bun'
# #         self.tikii = 'tikki'
# #
# #     def getBuger(self):
# #         return {
# #             "bun": self.bun
# #             , "tikki": self.tikii
# #         }
# #
# #
# # a = burger()
# # a.tikii = 'potato tikki'
# # burger.onion = 'banana'
# # print(a.onion)
# # print(a.getBuger())
# #
# # b = burger()
# # print(b.onion)
# # print(b.getBuger())
# # type()
#
#
# # def permutation(data, result=[]):
# #     if len(data) == 0:
# #         print(result)
# #     else:
# #         for i in range(len(data)):
# #             remain = data[:i] + data[i + 1:]
# #             permutation(remain, result + [data[i]])
# #
# #
# # def combination(data, r, result=[]):
# #     if len(data) == 0:
# #         print(result)
# #     else:
# #         for i in range(len(data)):
# #             combination(data[i], r - 1, result + [data[i]])
# #
# #
# # data = [1, 2, 4]
# # permutation(data)
#
# text= "{}"
text1 = 'sagar'


def check_validation(text):
    right = len(text) - 1
    left = 0
    while left < right:
        if text[left] != text[right]:
            return False
        right = right - 1
        left = left + 1
    return True


print(check_validation(text1))


def perm(text, result=[]):
    if len(text) == 0:
        print(result)
    else:
        for x in range(len(text)):
            reminder = text[:x] + text[x + 1:]
            perm(reminder, result + [text[x]])


print(perm([1, 2, 3], result=[]))
#
def clock_angle(hour, minute):
    # Ensure hour is within 12-hour format
    hour = hour % 12

    # Calculate the positions of the hour and minute hands
    minute_angle = minute * 6  # 6 degrees per minute
    hour_angle = (hour * 30) + (minute * 0.5)  # 30 degrees per hour + 0.5 degrees per minute

    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Find the smaller angle
    return min(angle, 360 - angle)


# Example usage
hour = 3
minute = 15
print(f"The angle at {hour}:{minute} is {clock_angle(hour, minute)} degrees.")
