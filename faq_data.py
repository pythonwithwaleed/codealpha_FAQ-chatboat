"""FAQ data for the ShopEasy chatbot.

Each entry is (question, answer, alternative phrasings / keywords).
The third field helps the bot match paraphrases such as
"where is my package?" -> "How can I track my order?".
To use a different topic, just replace this list.
"""

FAQS = [
    ("How can I track my order?",
     "Open 'My Orders' in your account and click 'Track'. A tracking link is also emailed once your order ships.",
     "where is my package parcel delivery status tracking number locate shipment"),

    ("How long does shipping take?",
     "Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days.",
     "how many days delivery time when will my order arrive delivery speed fast"),

    ("What is your return policy?",
     "You can return unused items within 30 days of delivery for a full refund.",
     "money back exchange send back policy days allowed to return"),

    ("How do I return a product?",
     "Go to 'My Orders', select the item, click 'Return', and print the prepaid label. Drop the parcel at any courier point.",
     "send something back return label how to return item exchange"),

    ("How long does it take to get a refund?",
     "Refunds are processed within 5-7 business days after we receive the returned item.",
     "money back reimbursement when will I get my money refund time"),

    ("Which payment methods do you accept?",
     "We accept Visa, Mastercard, PayPal, bank transfer, and cash on delivery.",
     "pay credit card debit card cards paypal cod how can I pay payment options"),

    ("Can I cancel my order?",
     "Yes. Orders can be cancelled from 'My Orders' before they are shipped.",
     "cancel cancellation stop my order change my mind undo purchase"),

    ("How do I reset my password?",
     "Click 'Forgot password' on the login page and follow the link we email you.",
     "forgot password can't log in login problem change password account access"),

    ("Do you ship internationally?",
     "Yes, we ship to over 50 countries. International delivery takes 7-14 business days.",
     "overseas abroad worldwide other countries outside international shipping"),

    ("How can I contact customer support?",
     "Email support@shopeasy.example or use live chat, available 9am-6pm, Monday to Saturday.",
     "help talk to someone phone email agent customer service reach you contact us"),

    ("Do you offer discounts or promo codes?",
     "Subscribe to our newsletter for a 10% first-order code and seasonal sale announcements.",
     "coupon voucher sale offer deal cheaper promotion discount code"),

    ("What should I do if I received a damaged item?",
     "Contact support within 48 hours with a photo of the damage and we will send a replacement or refund.",
     "broken defective faulty wrong item arrived damaged parcel replacement"),
]
