from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    """Main page with SIP calculator"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint for SIP calculation"""
    data = request.get_json()
    
    monthly_investment = float(data.get('monthlyInvestment', 0))
    expected_return_rate = float(data.get('expectedReturnRate', 0))
    time_period = int(data.get('timePeriod', 0))
    
    # Calculate total invested amount
    total_invested = monthly_investment * 12 * time_period
    
    # Calculate returns using compound interest formula for SIP
    # M × {[(1 + r)^n - 1] / r} × (1 + r)
    # where M is monthly investment, r is monthly rate, n is number of months
    monthly_rate = expected_return_rate / (12 * 100)
    months = time_period * 12
    
    estimated_returns = monthly_investment * ((pow(1 + monthly_rate, months) - 1) / monthly_rate) * (1 + monthly_rate)
    estimated_returns = estimated_returns - total_invested
    
    total_value = total_invested + estimated_returns
    
    return jsonify({
        'totalInvested': round(total_invested, 2),
        'estimatedReturns': round(estimated_returns, 2),
        'totalValue': round(total_value, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)