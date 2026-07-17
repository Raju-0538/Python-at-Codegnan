try:
    with open('output.txt','w') as file:
        for i in range(10):
            file.write(str(i)+" ")
except Exception as e:
    print(f"Something wrong : {e}")
