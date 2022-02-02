{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ab59bfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Number: 56\n",
      "The factorial of  0  is  710998587804863451854045647463724949736497978881168458687447040000000000000\n"
     ]
    }
   ],
   "source": [
    "fact = 1\n",
    "num = int (input(\"Enter the Number: \"))\n",
    "while num > 0:\n",
    "    fact = fact  * num\n",
    "    num = num - 1\n",
    "print (\"The factorial of \",num, \" is \",fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9ad60012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter any number : 45\n",
      "45 is NOT a prime number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enter any number : \"))\n",
    "if num > 1:\n",
    "    for i in range(2, num):\n",
    "        if num % i == 0:\n",
    "            print(num,\"is NOT a prime number\")\n",
    "            break\n",
    "    else:\n",
    "        print(num,\"is a PRIME number\")\n",
    "elif num == 0 or num == 1:\n",
    "    print(num,\"is NEITHER prime nor composite number.\")\n",
    "else:\n",
    "    print(num,\"is a PRIME number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "53b0f6ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a string34\n",
      "Not palindrome\n"
     ]
    }
   ],
   "source": [
    "s=input(\"Enter a string\")\n",
    "revstr=(s[::-1])\n",
    "if revstr==s:\n",
    "    print(\"palindrome\")\n",
    "else:\n",
    "    print(\"Not palindrome\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "abc61017",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input length of shorter triangle side: \n",
      "Enter a: 54\n",
      "Enter b:76\n",
      "the length of hypotenuse is: 93.23089616645332\n"
     ]
    }
   ],
   "source": [
    "from math import sqrt\n",
    "print(\"Input length of shorter triangle side: \")\n",
    "a = float(input(\"Enter a: \"))\n",
    "b = float(input(\"Enter b:\"))\n",
    "c = sqrt(a**2 + b**2)\n",
    "print(\"the length of hypotenuse is:\", c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2ce16de6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter any String 34\n",
      "Enter search Character 73\n",
      "Number of time Found = 0\n"
     ]
    }
   ],
   "source": [
    "na=input(\"Enter any String \")\n",
    "ch = input(\"Enter search Character \")\n",
    "f = 0\n",
    "for i in na:\n",
    "    if i == ch:\n",
    "        f=f+1\n",
    "print(\"Number of time Found =\",f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "686b50df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
