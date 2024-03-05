# Assignment 3a: NRIC

The Singapore NRIC number is made up of a leading letter, 7 digits, and a trailing letter. This letter is calculated from the first 7 digits using the modulus eleven method.

Write program code to:

1. Ask the user to input an NRIC number,
2. validate the check digit,
3. Print the validation result.

## Part 1: Validation rules

A valid NRIC number must obey the following rules:

1. The first letter must be S, T, F, or G (not case-sensitive).
2. There must be 7 numerical digits.
3. There must only be one letter after the 7 numerical digits.

Write program code to:

1. Ask the user to input an NRIC number,
2. validate the input according to the above rules,
3. Print the validation result.

### Expected output

    Enter an NRIC number: S1234567A
    NRIC format is valid.
    Enter an NRIC number: S123456B
    NRIC format is invalid.
    Enter an NRIC number: C1234567C
    NRIC format is invalid.

## Part 2: Check digit rule

This task builds on your code from Part 1.

The steps involved to obtain the check digit are:

1. Multiply each digit in the NRIC number by its weight (See Table 1).
2. Add the products from Step   1 together.
3. If the first letter is T or G, add 4 to the total in Step 2.
4. Divide the resulting sum in Step 2 by 11 and keep the remainder.
5. Check the check digit against the table to obtain the alphabet (See Table 2).

The following table shows the weight for each digit of the NRIC number:

    ┍━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━┑
    │Digit sequence  │ 1  2  3  4  5  6  7 │
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━┥
    │Digit weight    │ 2  7  6  5  4  3  2 │
    ┕━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━┙
    Table 1: Weight table for each NRIC digit

The following table is used to change the check digit into the corresponding alphabet.

    ┍━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    │Check Digit     │ 0  1  2  3  4  5  6  7  8  9 10  │
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
    │Starts with S/T │ J  Z  I  H  G  F  E  D  C  B  A  │ 
    ┝━━━━━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┥
    │Starts with F/G │ X  W  U  T  R  Q  P  N  M  L  K  │ 
    ┕━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
    Table 2: Check digit to alphabet conversion

### Validation reporting

The validation report should inform the user whether the NRIC string is valid. No reason needs to be provided.

Write program code to:

1. validate the check digit of the NRIC number,
2. Print the result of the NRIC validation (`valid` or `invalid` only)

The variable `nric` is still available to the below code if you run the code cell from Task 1 first.

### Expected output

    The input NRIC is S1234567A.
    NRIC is invalid.
    The input NRIC is S1234567D.
    NRIC is valid.
    The input NRIC is <your NRIC>.
    NRIC is valid.

# Submission

Before submission, run the tests on your final code.
