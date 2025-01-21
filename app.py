from flask import Flask, request, jsonify, render_template
import random
import re

app = Flask(__name__)


faqs = [
    {"pattern": r"business hours", "response": "Our business hours are Monday to Friday, 9 AM to 5 PM EST."},
    {"pattern": r"reset.*(password|pwd)", "response": "You can reset your password by clicking on the 'Forgot Password' link on the login page."},
    {"pattern": r"payment method", "response": "We accept Visa, MasterCard, American Express, and PayPal."},
    {"pattern": r"refund policy", "response": "Refunds can be requested within 30 days of purchase. Please contact support for assistance."},
    {"pattern": r"track.*order", "response": "You can track your order using the tracking number provided in your confirmation email."},
    {"pattern": r"support contact", "response": "You can reach our support team via email at support@example.com or call us at (555) 123-4567."},
    {"pattern": r"delivery time", "response": "Delivery times depend on your location and shipping method. Standard shipping typically takes 5-7 business days."},
    {"pattern": r"cancel.*order", "response": "To cancel an order, please log in to your account and navigate to the 'My Orders' section, or contact support directly."},
    {"pattern": r"discounts|promotions", "response": "We offer seasonal discounts and promotions. Subscribe to our newsletter to stay updated."},
    {"pattern": r"data privacy|security", "response": "We prioritize your data security and comply with all relevant privacy regulations. For details, check our Privacy Policy page."},
    {"pattern": r"product warranty", "response": "All our products come with a 1-year warranty. Please refer to the product documentation for specifics."},
    {"pattern": r"update.*(address|profile)", "response": "You can update your address or profile information in the 'Account Settings' section of your profile."},
    {"pattern": r"technical issue", "response": "If you're facing technical issues, try restarting the application. If the issue persists, contact our support team."},
    {"pattern": r"how to sign up", "response": "To sign up, click on the 'Sign Up' button at the top right corner of our homepage and follow the instructions."},
    {"pattern": r"subscription plan", "response": "We offer monthly and yearly subscription plans. Check our Pricing page for more details."},
    {"pattern": r"how to redeem coupon", "response": "You can redeem a coupon by entering the code during checkout in the 'Promo Code' section."},
    {"pattern": r"international shipping", "response": "Yes, we offer international shipping. Shipping times and costs vary by destination."},
    {"pattern": r"how to return item", "response": "To return an item, please follow the instructions on our Returns & Exchanges page or contact support."},
    {"pattern": r"bulk purchase discount", "response": "We offer discounts for bulk purchases. Contact sales@example.com for more details."},
    {"pattern": r"lost.*package", "response": "If your package is lost, please contact our support team immediately. We'll investigate and resolve the issue."},
    {"pattern": r"login issue", "response": "If you're having trouble logging in, ensure your email and password are correct. If the issue persists, reset your password or contact support."},
    {"pattern": r"product availability", "response": "Product availability is displayed on each product's page. Out-of-stock items may have an estimated restock date."},
    {"pattern": r"gift card", "response": "We offer digital gift cards in various denominations. You can purchase them on our website."},
]


general_responses = [
    "I'm here to help. What else would you like to know?",
    "Is there anything else I can assist you with?",
    "Do you have any other questions?",
    "I'm happy to help with any other inquiries.",
    "Let me know if there's anything more you need.",
    "Feel free to ask if you have more questions.",
    "I'm available to assist with any additional concerns.",
    "What else can I do for you today?",
    "Your satisfaction is our priority. Let me know how I can help further.",
    "Don't hesitate to reach out if you need anything else.",
    "I'm here to make things easier for you. Let me know how I can assist.",
    "Do you need clarification or help with anything else?",
    "I’d be glad to help with any further questions you have.",
    "Let me know if there's anything specific you'd like more information about.",
    "I'm always here to assist. What can I help with next?",
]


def get_bot_response(user_message):
    # Check FAQs
    for faq in faqs:
        if re.search(faq["pattern"], user_message, re.IGNORECASE):
            return faq["response"]

    # If no FAQ match, provide a general response
    return random.choice(general_responses)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)

