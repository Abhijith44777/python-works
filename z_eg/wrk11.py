# # def fibonaccy(num):
# #     prev = 0
# #     current = 1
# #     print(prev,current , end = " ")
# #     for i in range(1,num):
# #         next = prev + current
# #         prev = current
# #         current = next
# #         print(next, end= " ")
# # fibonaccy(10)
# # def fibonaccy(num):
# #     previous=0
# #     current=1
# #     print(previous,current,end="")
# #     for i in range(1,num):
# #         next=previous+current
# #         current=next
# #         previous=current
# #         print(next,end=" ")
# # fibonaccy(10)        

# # def fibonaccy(num):
# #     current=1
# #     previous=0
# #     print(previous,current,end=" ")
# #     for i in range(1,num):
# #         next=current+previous
# #         current=next
# #         previous=current
# #         print(next,end=" ")
# # fibonaccy(10)

# # # def palindrome(word):
# # #     word=word.casefold()
# # #     reversed_word=word[::-1]
# # #     print("palindrome" if word==reversed_word else "not palindrome")





# # def analyze_string(text):

# #     alphabet_count = 0
# #     space_count = 0
# #     special_char_count = 0
# #     number_count = 0
    
# # palindrome(input("enter word = "))
# # def fibonaccy(num):
# #     prev = 0
# #     current = 1
# #     print(prev,current , end = " ")
# #     for i in range(1,num):
# #         next = prev + current
# #         prev = current
# #         current = next
# #         print(next, end= " ")
# # fibonaccy(10)




# def analyze_string(text):
    
#     alphabet_count = 0
#     space_count = 0
#     special_char_count = 0
#     number_count = 0
    
#     for char in text:
#         if char.isalpha():
#             alphabet_count += 1
#         elif char.isspace():
#             space_count += 1
#         elif char.isdigit():
#             number_count += 1
#         else:
#             special_char_count += 1
    
#     return {
#         "alphabet_count": alphabet_count,
#         "space_count": space_count,
#         "special_char_count": special_char_count,
#         "number_count": number_count
#     }
#     print(analyze_string(input("enter word")))

# employee id,name,department,age,salary
# employee={"id":101,"name":"hari","department":"sales","age":55}

# print(employee)
# print(employee.get("department"))
# print(employee["id"])
# employee["salary"]=37890
# print(employee)
# if salaryin employee:
add=lambda n1,n2:n1+n2

print(add(10,5))

add=lambda n1,n2:n1+n2
print(add(66,34))

sub=lambda n1,n2:n1-n2
print(sub(66,6))