1. For Loop --> every point in a certain range is visited
  for i in range(1,5): this line means visiting [1,2,3,4]
2. While Loop --> loop keeps executing until the condition is true
example: hungry = True
         while hungry:
             print("Eating hay...")
            hungry = False # Okay, I'm full now. Stop!
3. Break --> I'm done...stop execution
example:for step in range(1, 100):
            if step == 5:
            print("I'm tired. Stopping at step 5.")
            break # The loop ends right here!
        print("Walking...")
4. Continue --> when you want to skip something yikes!!
        for food in ["apple", "rotten carrot", "banana"]:
            if food == "rotten carrot":
            continue 
         print("Eating:", food)
        
5. Default rules of range():
    i) range(3) means loop starts at 0, stops at 2 --> 0,1,2
    ii) range(1,3) means starts at 1, stops at 2 --> 1,2
    iii) by default range increments steps by 1
         negative increment indicated iterating from larger values to smaller values,start point>end point
    iv) range(5,9,2); here increment is done by 2 --> 5,7
    v) range(3,0,-1) ;Starts at 3, walks back, stops before 0 -->3,2,1
6. Nested Loop --> loop inside another loop 
    for i in range(3):
        print("I am innocent")
        for j in range(3):
            print("We are having retrials!!!")
7. Infinite Loops --> loops continues forever
     while True:
        print("Dreaming of a world where my code has zero bugs...")


|  Loop Type |                       Best Use Case |
| :---: | :---- |
| **while**  | When the number of iterations is **unknown**depends on a **condition** (e.g., user input, until a flag is set). |
| **for** | When **you know exactly how many times to iterate** (e.g., **over a list, a fixed range**). |



        
