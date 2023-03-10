from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
complaint_sentences = [
    'I want to file a complaint',
    'I want to log a ticket',
    'I want to report a bug',
    'I want to report a problem',
    'I want to log a problem',
    'I want to issue a ticket',
]

appointment_sentences = [
    'I want to book an appointment',
    'I want to schedule an appointment',
    'I want to make an appointment',
    'I want to book a meeting',
    'I want to talk to support'
]


def calculateSentiment(text):
    complaint_embeddings = model.encode(
        complaint_sentences+[text])
    appointment_embeddings = model.encode(
        appointment_sentences+[text])

    complaint_cosine_scores = util.pytorch_cos_sim(
        complaint_embeddings[-1], complaint_embeddings[:-1])
    appointment_cosine_scores = util.pytorch_cos_sim(
        appointment_embeddings[-1], appointment_embeddings[:-1])
    c_avg = complaint_cosine_scores.mean()
    # print average of appointment
    a_avg = appointment_cosine_scores.mean()
    threshold = 0.6

    if c_avg > threshold and a_avg > threshold:

        if c_avg > a_avg:
            sentiment = 'complaint'
        else:
            sentiment = 'appointment'
    else:
        sentiment = 'none'

    return sentiment
