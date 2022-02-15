sampleList = [1,2,3,4,5]
age = 10
percent = "99.14A"
print("Statement before Error")
try:
    print(sampleList[1])
    value = sampleList[2] / age
   # float_percent = float(percent)
except Exception as ex:
    print("All the errors now handled with this", type(ex))
except (IndexError, ArithmeticError) as err:
    print("There was an Error", type(err))
else:
    print("This statement means - try safely completed")
finally:
    print("This section will always execute")


print("Statement After Error")

'''
1. except
2. except Error
3. Multiple except
4. Combine errors in except
5. Specific first , generic later - except

try:
    block of code - risky 
    might generate an error
except:
    block of code which will execute if error occurs
except SpecificError:
    another logic of handling different error
else:
    block of code execute only if try completes
    it has to be before finally
finally:
    block of code which will execute regardless of error
'''

# How to throw an error from a method
# Writing and using Custom Errors