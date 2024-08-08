from flask import Flask, render_template, request
import pickle


model = pickle.load(open('fuel.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/y_predict',methods=['POST','GET'])
def y_predict():
    return render_template('y_predict.html')


@app.route('/result', methods=['GET','POST'])
def predict():
    print(request.method)
    if request.method == 'POST' :
        x_test=[[float(x) for x in request.form.values()]]
        print('actual',x_test)
        pred=model.predict(x_test)
        return render_template('result.html', \
                            prediction_text=('Car fuel Consumption(L/100km) \
                                                : ',pred[0]))
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)