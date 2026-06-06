import random

def game():
    # สุ่มตัวเลขระหว่าง 1 ถึง 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("=== ยินดีต้อนรับสู่เกมทายตัวเลข! ===")
    print("ฉันได้สุ่มตัวเลขระหว่าง 1 ถึง 100 ไว้แล้ว มาลองทายกันเลย!")

    while True:
        try:
            guess = int(input("ใส่ตัวเลขที่คุณทาย: "))
            attempts += 1

            if guess < secret_number:
                print("น้อยเกินไป! ลองใหม่อีกครั้ง")
            elif guess > secret_number:
                print("มากเกินไป! ลองใหม่อีกครั้ง")
            else:
                print(f"🎉 ยินดีด้วย! คุณทายถูกแล้ว เลขนั้นคือ {secret_number}")
                print(f"คุณใช้จำนวนครั้งในการทายทั้งหมด {attempts} ครั้ง")
                break
        except ValueError:
            print("กรุณาใส่เฉพาะตัวเลขเท่านั้นนะ!")

if __name__ == "__main__":
    game()
