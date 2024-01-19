fruits = ["Apple", "Orange", "Grape"]
fruits.append("Berry")

# for i in fruits:
#     print(f'Fruit is : {i}')


# Break
# for i in fruits:
#     if i == "Apple":
#         break
#     print(f'Fruit is : {i}')

# Continue
# for i in fruits:
#     if i == "Orange":
#         continue
#     print(f'Fruit is : {i}')
# print("hello")

# range(10)
# range(0, 10)

for i in range(10):
    print(f'i : {i}')

count = 0  # step 1
while count < len(fruits):
    print(f'Fruit is : {fruits[count]}')  # fruits[2]
    count += 1

# count = 0
# while 0<4 => print(fruits[0])
# count = 0 + 1
# while 1<4 => print(fruits[1])
# count = 1 + 1
# while 2<4 => print(fruits[2])
# count = 2 + 1
# while 3<4 => print(fruits[3])
# count = 3 + 1
# while 4<4 => quit loop


# count = 0
# while count < 10:
#     print(f'Count: {count}')
#     count += 1 # count = count + 1
