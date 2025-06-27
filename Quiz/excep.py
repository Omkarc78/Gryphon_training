

class MyError(Exception):
    pass

def excep():
    while True:
        try:
            user_ans = input("Enter your answer: ")
            if not user_ans.strip().isdigit():
                raise MyError("Input is not a number!")
            return int(user_ans)
        except MyError as e:
            print("Caught error:", e)
