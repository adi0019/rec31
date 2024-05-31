from flask import Flask, request, jsonify
import language_tool_python
import enchant
from nltk import word_tokenize, sent_tokenize
from googleapiclient.discovery import build

app = Flask(__name__)

def grammar_and_spelling_checker(text):
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]

    # Load the English language dictionary for spelling checking
    english_dict = enchant.Dict("en_US")

    # Initialize language_tool_python for grammar checking
    tool = language_tool_python.LanguageTool('en-US')

    spelling_errors = 0
    grammar_errors = 0
    error_messages = []
    corrected_sentences = []

    # Check grammar and spelling for each word
    for sentence in words:
        corrected_sentence = []

        for word in sentence:
            # Check for spelling errors
            if not english_dict.check(word):
                spelling_errors += 1
                suggestions = english_dict.suggest(word)
                error_messages.append(f"Spelling error: {word}, Suggestions: {', '.join(suggestions)}")
                # Use the first suggestion if available, otherwise keep the original word
                corrected_sentence.append(suggestions[0] if suggestions else word)
            else:
                corrected_sentence.append(word)

        # Join the words back into a sentence for grammar checking
        sentence_text = ' '.join(corrected_sentence)

        # Check for grammar errors
        matches = tool.check(sentence_text)
        grammar_errors += len(matches)

        for match in matches:
            error_messages.append(f"Grammar error: {match.ruleId} - {match.message}")

        # Append the corrected sentence
        corrected_sentences.append(sentence_text)

    # Calculate accuracy
    accuracy = calculate_accuracy(text, ' '.join(corrected_sentences))

    return spelling_errors, grammar_errors, error_messages, corrected_sentences, accuracy

def calculate_accuracy(original_text, corrected_text):
    original_tokens = word_tokenize(original_text)
    corrected_tokens = word_tokenize(corrected_text)
    correct_count = sum(1 for orig, corr in zip(original_tokens, corrected_tokens) if orig == corr)
    accuracy = (correct_count / len(original_tokens)) * 100
    return accuracy

def count_words(text):
    words = word_tokenize(text)
    return len(words)

def suggest_video(acc):
    print("accuracy", acc)
    # Set up the YouTube API key
    api_key = "AIzaSyD_ZApgZ7kS2cAo8yUdeWCEhU1OQL9gsqw"
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search for videos related to grammar
    def search_videos(query, max_results=7):
        request = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        return response['items']

    if 0 < acc <= 10 :
        query = "Introduction to English grammar,Beginner English grammar lessons"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr   
    elif 10 < acc <= 20 :
        query = "Basic English grammar exercises,Common English grammar mistakes"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 20 < acc <= 30 :
        query = "Advanced English grammar rules,English grammar tips and tricks"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 30 < acc <= 40 :
        query = "English verb tenses explained,Understanding English grammar structures"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 40 < acc <= 50 :
        query = "Correct use of English prepositions,Mastering English grammar concepts"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 50 < acc <= 60 :
        query = "Subject-verb agreement in English,Improving English sentence construction"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 60 < acc <= 70 :
        query = "English adjectives and adverbs usage,Refining English grammar skills"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 70 < acc <= 80 :
        query = "English articles (a, an, the) rules,Perfecting English grammar and punctuation"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 80 < acc <= 85 :
        query = "Perfecting English grammar and punctuation,adjectives and adverbs usage,Refining English grammar skills"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 85 < acc <= 90 :
        query = "English grammar for professional communication,usage of tenses,Advanced English grammar exercises,Punctuation rules in English"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 90 < acc <= 95 :
        query = "English sentence structure and syntax,verb tenses,Punctuation rules in English,Advanced English grammar exercises"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr  
    elif 95 < acc <= 100 :
        query = "Mastering complex English grammar concepts,Expert-level English grammar lessons,English sentence structure and syntax"
        videos = search_videos(query)
        arr = []
        for video in videos:
            video_info = {
            "Title": video['snippet']['title'],
            "Image": f"https://i.ytimg.com/vi/{video['id']['videoId']}/default.jpg",
            "URL": f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            }
            arr.append(video_info)
        return arr    

        
@app.route('/', methods=['GET'])
def hello():
    return "THIS IS AN API."

@app.route('/check_spelling_and_grammar', methods=['POST'])
def check_spelling_and_grammar():
    data = request.json
    text = data.get('text', '')
    spelling_errors, grammar_errors, errors, corrected_sentences, accuracy = grammar_and_spelling_checker(text)
    response = {
        "spelling_errors": spelling_errors,
        "grammar_errors": grammar_errors,
        "errors": errors,
        "corrected_sentences": corrected_sentences,
        "accuracy": accuracy,
    }
    return jsonify(response)

@app.route('/count_words', methods=['POST'])
def count_words_endpoint():
    data = request.json
    text = data.get('text', '')
    word_count = count_words(text)
    response = {
        "word_count": word_count
    }
    return jsonify(response)

@app.route('/suggest', methods=['POST'])
def suggested_videos():
    data = request.json
    text = data.get("accuracy", "")
    suggest = suggest_video(text)
    response = {
        "suggested_videos": suggest
    }
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True)

