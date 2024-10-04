question1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096] # Multiply these with a for loop
question2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177] # Add these with a while loop
question3 = [.146, .875, .911, .083, .81, .439, .44, .05, .46, .76, .61, .68, .01, .14, .38, .26, .21] 

def answer1():
    result = 1
    for num in question1:
        result *= num
    print(result)

def answer2():
    result = 1
    while len(question2) != 0:
        result += question2.pop()
    print(result)

answer1()
answer2()