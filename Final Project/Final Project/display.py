from flask import Flask 
 
import redis 
 
app = Flask(__name__) 
 
@app.route('/') 
def print_logs():
    output = ''
    try:
        conn = redis.StrictRedis(host='redis', port=6379)

        vowelCount = 0
        nonVowelCount = 0
        sailorCount = 0
        windowCount = 0

        for key in conn.scan_iter("log.greeter_server*"):
            value = str(conn.get(key))	
        #    output += str(key) + value + '<br>'


            data = value.replace("'", " ").replace("b", " ").split()

            if("vowel" in data):
                
                vowelCount = vowelCount + 1
                 #print(vowelCount)

            else:
                  nonVowelCount = nonVowelCount + 1

            if("sailor" in data):
                
                sailorCount = sailorCount + 1
              #  print('-----' , sailorCount)

            if("window" in data):
                
                windowCount = windowCount + 1
              #  print('------------' , windowCount)


            stats = str(vowelCount), ':' , str(nonVowelCount) , 'vowels to non-vowels, Sailors: ', str(sailorCount), ' windows: ', str(windowCount)
         #   print(stats)
            output += str(key) + str(stats) +  '<br>'

            

    except Exception as ex:
        output = 'Error:' + str(ex)
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
