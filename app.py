from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Home redirects to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        withdraw_password = request.form['withdraw_password']

        # Save to database (we will add db later)
        print(f"Registered: {full_name}, {email}")

        return "Registered successfully! (This is a temporary message)"
    
    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authenticate user (database logic will be added later)
        print(f"Login attempt: {email}")

        # Simulate login success
        session['user'] = email
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

# Dashboard page (after login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user_info = {
            'full_name': 'John Doe',
            'email': session['user'],
            'balances': {
                'BTC': 0.0,
                'ETH': 0.0,
                'USDT': 0.0,
                'BNB': 0.0
            },
            'deposit_addresses': {
                'BTC': 'bc1qrynf3yt0w524mtca7q0t8hs4ufpd8fj5dg2855',
                'ETH': '0xe184F8F7112bF1471b9c4452Efb7Bf9E5ddb7df1',
                'USDT': '0xe184F8F7112bF1471b9c4452Efb7Bf9E5ddb7df1',
                'BNB': '0xe184F8F7112bF1471b9c4452Efb7Bf9E5ddb7df1'
            }
        }
        return render_template('user/dashboard.html', user=user_info)
    else:
        return redirect(url_for('login'))

    
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/trade')
def trade():
    return render_template('user/trade.html')


@app.route('/user/deposit')
def deposit():
    return render_template('user/deposit.html')

@app.route('/user/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        # Handle withdraw form
        pass
    return render_template('user/withdraw.html')
@app.route('/transaction_history')
def transaction_history():
    return render_template('user/transaction_history.html')

@app.route('/profile')
def profile():
    return render_template('user/profile.html')

@app.route('/kyc')
def kyc():
    return render_template('user/kyc.html')



if __name__ == '__main__':
    app.run(debug=True)
