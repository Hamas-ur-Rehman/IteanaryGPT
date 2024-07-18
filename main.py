
import openai
import dotenv
from prompts import *
import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime



dotenv.load_dotenv()

client = openai.OpenAI()
model = "gpt-4-1106-preview"

def activities(query: str) -> str:
    start_time = time.time()
    """to generate activities JSON"""
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  ACTIVITY_MODULE},
            {"role": "system", "content":  GOLDEN_RULES},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR only activities ignore everything else\n {EXAMPLES}"},
            {"role": "user", "content": query},
        ]
    )
    print("ACTIVITIES GENERATED --- %s seconds ---" % (time.time() - start_time))
    return response.choices[0].message.content

def transport(query: str) -> str:
    """to generate transport JSON"""
    start_time = time.time()
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  TRANSPORT_MODULE},
            {"role": "system", "content":  GOLDEN_RULES},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR only transport ignore everything else \n {EXAMPLES}"},
            {"role": "user", "content": query},
        ]
    )
    print("TRANSPORTATION GENERATED--- %s seconds ---" % (time.time() - start_time))
    return response.choices[0].message.content

def experience(query: str) -> str:
    """to generate experience JSON"""
    start_time = time.time()
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  EXPERIENCE_MODULE},
            {"role": "system", "content":  GOLDEN_RULES},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR only experience ignore everything else \n {EXAMPLES}"},
            {"role": "user", "content": query},
        ]
    )
    print("EXPERIENCES GENERATED--- %s seconds ---" % (time.time() - start_time))
    return response.choices[0].message.content

def accommodation(query: str) -> str:
    """to generate accommodation JSON"""
    start_time = time.time()
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  ACCOMMODATION_MODULE},
            {"role": "system", "content":  GOLDEN_RULES},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR only accomodation ignore everything else \n {EXAMPLES}"},
            {"role": "user", "content": query},
        ]
    )
    print("ACCOMODATION GENERATED--- %s seconds ---" % (time.time() - start_time))
    return response.choices[0].message.content

def food(query: str) -> str:
    """to generate food JSON"""
    start_time = time.time()
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  FOOD_MODULE},
            {"role": "system", "content":  GOLDEN_RULES},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR only Food ignore everything else \n {EXAMPLES}"},
            {"role": "user", "content": query},
        ]
    )
    print("FOOD GENERATED--- %s seconds ---" % (time.time() - start_time))
    return response.choices[0].message.content

def ask(query: str) -> str:
    """Convert query to a new format prompt"""
    start_time = time.time()
    prompt = f"""Using the following query, please convert it to a new format prompt:
    use best of your knowledge to generate the start and end dates using the current date and number of days
    Location: 
    Number of Days:
    Current Date: {datetime.now().strftime("%d/%m/%Y")}
    Start Date:
    End Date:
    Other Details:
    Actual Query: {query}"""    
    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":prompt },
            {"role": "user", "content": query},
        ]
    )
    new_prompt = response.choices[0].message.content+" KEEP TRACK OF THE NUMBER OF DAYS"
    print(new_prompt)
    execute_bots = []

    with ThreadPoolExecutor() as executor:
        activities_future = executor.submit(activities, new_prompt)
        transport_future = executor.submit(transport, new_prompt)
        experience_future = executor.submit(experience, new_prompt)
        accommodation_future = executor.submit(accommodation, new_prompt)
        food_future = executor.submit(food, new_prompt)


    execute_bots.append (activities_future)
    execute_bots.append (transport_future)
    execute_bots.append (experience_future)
    execute_bots.append (accommodation_future)
    execute_bots.append (food_future)



    concurrent.futures.wait(execute_bots)

    data = {
    "activities": activities_future.result(),
    "transport": transport_future.result(),
    "experience": experience_future.result(),
    "accommodation": accommodation_future.result(),
    "food": food_future.result()
    }

    response =  client.chat.completions.create(
        temperature = 0,
        model=model,
        messages=[
            {"role": "system", "content":  CONTEXT+TECHNICAL_CONTEXT},
            {"role": "system", "content": f"THESE EXAMPLES ARE FOR YOU TO UTILIZE AND FILL IN YOUR DATA WHERE YOU THINK IT MIGHT HELP FOR activities, transport, experiences, accommodation, food {EXAMPLES}"},
            {"role": "system", "content": f"Follow these Golden Rules: {GOLDEN_RULES}"},
            {"role": "system", "content": f"This is the generated data: {data}"},
            {"role": "user", "content": query},
            {"role": "user", "content": f"KEEP TRACK OF THE NUMBER OF DAYS Generate the final JSON make sure to have all these fields : activities, transport, experiences, accommodation, food"},
        ]
    )
    
    print("ITEANARY GENERATED --- %s seconds ---" % (time.time() - start_time))
    with (open("output2.json", "w",encoding='utf-8')) as f:
        f.write(response.choices[0].message.content)
    return response.choices[0].message.content

        



ask("HoChiMinh 3 days")
