

Diffie–Hellman key exchange (DH) is a method of securely exchanging cryptographic keys over a public channel 





Consider two friends, Poonam and Neelam, both want to share some confidential data over an insecure channel 
which is susceptible to public inteference.
Another person, Rashmi, an evesdropper, is trying to break into the communication and get the data.

However, Neelam has an idea with which she and Poonam can securely exchange the data without Rashmi's knowledge.
She uses the concept of DISCRETE LOGARITHM along with DIFFIE-HELLMAN KEY EXCHANGE mechanism, which is explained below:

So, there is these two numbers, p and g :
          p = 23
          g = 5
          
this pair (p,g) is publicly available (that means Rashmi also has access to this)


Neelam chooses a secret number "a" and a = 6.
She sends  A = g^a mod p  to Poonam.
          =>> A = 5^6 mod 23 
          =>> A = 8


Poonam also chooses another secret number "b" and b = 15
She sends  B = g^b mod p this to Neelam.
          =>> A = 5^15 mod 23
          =>> A = 19

But Rashmi has access to these two, A and B  but not "a" and "b".

Now, Poonam does the following maths:
          She received A = 8 and exponentiated it with her secret number, i.e. 
                    8^15 and takes the mod with p;
                            8^15 mod 23 = 2.
                            
Now, Neelam also performs the same:
          She received B = 19 and exponentiated it with her secret number, i.e. 
                    19^6 and takes the mod with p;
                            19^6 mod 23 = 2. 
                            
                            
   So, now both Neelam and Poonam, have the key without being Rashmi involved in the transaction.
   The exchange proves to be fruitful to the two friends, and leaves Rashmi perplexed in her calculations.
   
   
   
   
   
                            
            
