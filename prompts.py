CONTEXT ="""You are an expert travel planner for Holicay, a leading travel agency known for its personalized trip planning using a kanban canvas. This canvas breaks down the trip into different days, with specific activities, food and beverage recommendations, paid experiences, transportation options, and accommodations. 
    With almost 30 years of experience in trip planning, you have developed the skills to cater to each customer's unique needs. Your goal is to create highly customized itineraries by considering factors such as timing, module titles, descriptions, duration in each city, and your own expertise. To achieve this, you rely on data from past itineraries provided in JSON format. You use this data to learn and adapt, generating output in JSON format that can be integrated back into the Kanban canvas for Holicay
"""
TECHNICAL_CONTEXT = """The output of this prompt should be in JSON format. To ensure that you plan a feasible and logical trip for the customer, we will provide a list of our top itineraries in the next section. However, these itineraries will be presented to you in a printed JSON format, as they appear on our platform's canvas view. Each itinerary will include the following types of information. There are 5 different modules that will be displayed in the JSON format. It is important to understand the context behind each module so that you can comprehend why the itinerary was arranged in a specific way when reviewing it in detail.
"""

ACTIVITY_MODULE = TECHNICAL_CONTEXT + """\nACTIVITY MODULE:
    Activity modules are representative of a specific visit to a landmark e.g. eiffel tower, berlin wall, hanoi old quarter. If this are included into an itinerary, it means that the customer will be only visiting that specific place/landmark from that start time and for that specific duration. When deciding which activities to put for a specific day, you need to screen through all the parameters in the json format to make a decision. 

    EXAMPLE JSON FORMAT FOR ACTIVITY MODULE:
    -------------------------------
    "activities": [
            {
                "name": "Ben Thanh Market",
                "category": "Landmarks",
                "address": {
                    "position": {
                        "lat": 10.7725168,
                        "lng": 106.6980208
                    },
                    "label": "Ben Thanh, District 1, Ho Chi Minh City, Vietnam"
                },
                "startDate": "2024-02-27T00:00:00.000Z",
                "startTime": "08:00",
                "duration": 60,
                "ActivityId": "ChIJTeYpMT8vdTERMH8sUnkta40"
            },]




    AN EXAMPLE COULD BE LIKE THIS FOR A SPECIFIC NUMBER OF DAYS TRIP
 "activities": [
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJDFj42q4VVHVm_gSqUgKz1Or9J3miKt1H4tJLqsMhWzg13UiiG1XsxxxpEYISBQyIk03QwKISIux8fem7dtbN0UIW8Rj0BPtBk6_sQ=s1600-w800"
            ],
            "name": "Ben Thanh Market",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7725168,
                    "lng": 106.6980208
                },
                "label": "Ben Thanh, District 1, Ho Chi Minh City, Vietnam"
            },
            "startDate": "2024-02-27T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJTeYpMT8vdTERMH8sUnkta40",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJQcZqJQ-w5d79Sp0C6d2wTVvmPTXnUccWsxS1MM4X6fN0U9fTWemfzVq3f9Kmkw4S5wNj7b1pyLvYDwywubytFLnNWCHpWl3hkUFBk=s1600-w800"
            ],
            "name": "Ho Chi Minh City Museum of Fine Arts",
            "category": "Culture and history",
            "address": {
                "position": {
                    "lat": 10.7699332,
                    "lng": 106.6991155
                },
                "label": "97A P. Đức Chính, Phường Nguyễn Thái Bình, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-27T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJsfntd0AvdTERdgUjB_drRrE",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AM5lPC8-ojERY6s94p-mpmsANIgH0hiYk6kB0BXRv3WP8twJNYpci_6hwiq1lEEre8mrLLRZxVqNPWYQsPMAzmA6mZ6vkbP7rQXMqx4=s1600-w800"
            ],
            "name": "Bui Vien Walking Street",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7674231,
                    "lng": 106.6939905
                },
                "label": "Đ. Bùi Viện, Phường Phạm Ngũ Lão, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-27T00:00:00.000Z",
            "startTime": "10:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJCdzLBRYvdTERpsMyNScNwPE",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANXAkqFvcRCexAn9kpfXRdzRcxLzvGbJHv1ULRKPW96g7L96yFRoNvxrfxaOJ7H8dmuUvVwxzKJPuyzAjawut12SxWRlqAi_BVSNfKw=s1600-w800"
            ],
            "name": "September 23rd Park",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7688009,
                    "lng": 106.6921297
                },
                "label": "Đ. Phạm Ngũ Lão, Phường Phạm Ngũ Lão, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-28T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJu4YK_j4vdTERfSn0egKOyug",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3Dt0tZuguS3K0_LU3lgJ3lHfrRsQhDwPxdzVLSeTkYfSHYQ_TG_kQGiX7uBz-qXjt15BZGXKhUQCDWWIj6rHnmUuxUFPFWGLO9s=s1600-w564"
            ],
            "name": "Tao Dan Park",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7745379,
                    "lng": 106.6924421
                },
                "label": "Ben Thanh, District 1, Ho Chi Minh City, Vietnam"
            },
            "startDate": "2024-02-28T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJsXOVajkvdTERcBdP0Xow8j4",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AM5lPC86DwHOELqAEJjT4yMjMZo9AoSH-RdUjan_jCG-fkF-W0fr-rAgFkJjDAAP61Gr7FPFvFykVR0SU3Rq60dfB7vgmAWM2QSTQWE=s1600-w789"
            ],
            "name": "Independence Palace",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7769942,
                    "lng": 106.6953021
                },
                "label": "Ben Thanh, District 1, Ho Chi Minh City, Vietnam"
            },
            "startDate": "2024-02-28T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJL0dwVTgvdTERao3t8B1Jhxc",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AM5lPC_fRVVJKqFrOUOOMXiGbB0xPSbTyhoyPyEXIWN0Ad1J85aC1dUxlNr-_r9tx1k_TqToJ5C711nlarzqFdWZuIpreaMfqD6sJlg=s1600-w800"
            ],
            "name": "Notre Dame Cathedral of Saigon",
            "category": "Culture and history",
            "address": {
                "position": {
                    "lat": 10.7797855,
                    "lng": 106.6990189
                },
                "label": "01 Công xã Paris, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh 70000, Vietnam"
            },
            "startDate": "2024-02-29T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJUSTY5jcvdTERRVvtbJNZT-g",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DsWn2-BeNyqCyQcuVu4NAxSrNzzA5EJOpap2LsnLC8KsYjR0576yv6cvQGO_AB1mLr6iUdsUGvsBdfK9cHVI-UHYdsJE7EggvE=s1600-w800"
            ],
            "name": "Ho Chi Minh City Book Street",
            "category": "Shopping",
            "address": {
                "position": {
                    "lat": 10.7809702,
                    "lng": 106.700107
                },
                "label": "Đường Nguyễn Văn Bình, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-29T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJS8Yv1zcvdTERUI2V47UxkPw",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJDFj434ppoeLqPlR1GqxqakyaO1XkPXfzLSDlFzcro9hmKvmOWYnbAleCO4LRIgXSun_0YcfxQt-zpZ_6A4ZotHTnHbnccZGqnqKLY=s1600-w800"
            ],
            "name": "History Museum of Ho Chi Minh City",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.787984,
                    "lng": 106.7047376
                },
                "label": "2 Nguyễn Bỉnh Khiêm, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-29T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJ5fqrRUsvdTERlfW0JX8JGyU",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJQcZqLg_d_-psyHmA83aBeFKEp1pgB49LYLsantTClznYRIYs06RI71LISrU9S4JdypYXV8_4n6nOyydheR3DgkgvFBpP11moNC5wA=s1600-w800"
            ],
            "name": "Saigon Zoo and Botanical Garden",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7875434,
                    "lng": 106.7052906
                },
                "label": "2 Nguyễn Bỉnh Khiêm, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh 700000, Vietnam"
            },
            "startDate": "2024-03-01T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJx7wwM0svdTERjuH2a9dkuU0",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DsXhzmCCcIC1gLj-rD78acyNI3awAKRD1GIZYTfF33HJv3kVsSs-f6YSMGZg8nxePcxD-qDEgZK1qoJ-5Qv00Yri9d8UAp88m8=s1600-w800"
            ],
            "name": "Van Thanh Tourist Park",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7981787,
                    "lng": 106.7157267
                },
                "label": "48/10 Đ. Điện Biên Phủ, Phường 22, Bình Thạnh, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-01T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJV8BHDV0pdTERvGqxdSId_50",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANXAkqHfov1YdPPH9GdZN5bBEV798-LHZqdswt7dEjSttR4tsp3JHLOsrBIe1Hy9z67RvFcdoVOknwu1nRtObaJU9592RmjFoDN5dQ=s1600-w800"
            ],
            "name": "Ben Bach Dang Park",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7727276,
                    "lng": 106.7067045
                },
                "label": "1 Đ. Tôn Đức Thắng, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-01T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJqVawLjgvdTERy0WoSbe7qgA",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANXAkqHPKSIEF9qKmUalKWazjwcFXvd3OeacbNT6hIk7eSpQ2RBdkJK9CvxpKmLC3FBVIE5Z0lmUn44BpKEXMml18a5qHgrOlyp-PNU=s1600-w800"
            ],
            "name": "Saigon Skydeck",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7715673,
                    "lng": 106.7042465
                },
                "label": "36 Đ. Hồ Tùng Mậu, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-02T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJVZKCP0EvdTERfHvs6AfGjok",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DvxrYXhLqwnaamjnlb0O1h1gxOGuyWTnWSDcaZxF8ctoj5dwDdtBpZUDd29Z4-S6BgqlTsBXcfdmhXRNiss9_mSAjkydUmgdSs=s1600-w800"
            ],
            "name": "Ho Chi Minh City Opera House",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7766352,
                    "lng": 106.7031654
                },
                "label": "07 Công Trường Lam Sơn, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh 710212, Vietnam"
            },
            "startDate": "2024-03-02T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJKcrnSUYvdTERO64MErYx9VU",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJQcZqKpBu55kTpuqFs7aK7dNMh4Wwb6tpq_T7AYEqC9OoHySxEguXuAs8QQ-UyS8zheSTnG0ztPSYLWa_NtTSOjfOD3VVH1rEl552U=s1600-w800"
            ],
            "name": "Ho Chi Minh Statue",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7760193,
                    "lng": 106.7015489
                },
                "label": "110 Đ. Nguyễn Huệ, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-02T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJlbodo0cvdTER54riaI9uWl0",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJDFj41WdLroM79MGeER04x_o-L-Tf-JeCGSizurkX4-NApV30gkga5ythOCNWmEJ1D-ywRA7qh_EQ21a7sQRwExs9YyLYZlqmGwq0Y=s1600-w800"
            ],
            "name": "War Remnants Museum",
            "category": "Culture and history",
            "address": {
                "position": {
                    "lat": 10.7795106,
                    "lng": 106.6920916
                },
                "label": "Phường 6, District 3, Ho Chi Minh City 700000, Vietnam"
            },
            "startDate": "2024-03-03T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJzwg3ojAvdTERqnQUK99K2Xw",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DtGvoqIzdP0CIR4P3JR1dUOCAXx2vttDl4ADVLsng21YxlnYwZH6YJWVj7Il8DqlUsJ3KCy_Oo0nAvICyAo-mcKQpRd25c2tQI=s1600-w800"
            ],
            "name": "Tan Dinh Market",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7896995,
                    "lng": 106.6898374
                },
                "label": "336 Hai Bà Trưng, Phường Tân Định, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-03T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJvxShM80odTER8eFLlfwiq48",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AJQcZqJNnl-VQDEHAphe5Mi8krZtOzXdZrEYGv25wvajs0mslYanC_bPZ5Mxyr00ZgO8QOnMRnLRMfj1e6OADAFsYfgqeYMVjkI30R8=s1600-w800"
            ],
            "name": "Museum of Traditional Vietnamese Medicine",
            "category": "Landmarks",
            "address": {
                "position": {
                    "lat": 10.7761979,
                    "lng": 106.6719075
                },
                "label": "41 Hoàng Dư Khương, Phường 12, Quận 10, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-03T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJC044E9kudTERi2Ozcof-Was",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/AM5lPC-03Nl6OCJfSlcd_UgEFzto72fBT6PCtRHH8MwPDBA0iVJaJeIXeSeqMP7VJ8D_roXRtAdSPtP68vj0ZU_r75fGnU1ZnKZL8Ig=s1600-w407"
            ],
            "name": "Dam Sen Water Park",
            "category": "Entertainment",
            "address": {
                "position": {
                    "lat": 10.7688947,
                    "lng": 106.6359939
                },
                "label": "3 Hòa Bình, Phường 3, Quận 11, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-03-04T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJ4RqUkJkudTER-QHI35eZcWI",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DuBl9xTq4rp0xYPHEVlONql3FBppv2WZ7SyaieyK5qhk3-RPlWOTJJZsVAypaLn9sCl8IhEnLy5F372ncTEKE3cALOxjiixGjI=s1600-w800"
            ],
            "name": "Cu Chi Tunnel",
            "category": "Culture and history",
            "address": {
                "position": {
                    "lat": 11.141591,
                    "lng": 106.4615963
                },
                "label": "Phú Hiệp, Củ Chi, Ho Chi Minh City, Vietnam"
            },
            "startDate": "2024-03-04T00:00:00.000Z",
            "startTime": "08:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJKXVC7sAyCzERLxR747WgrZg",
            "purchaseLink": ""
        },
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANXAkqFRty07IFP3QfPXMApKQ9CbKPqUczWAdOhgbp2NEvGEN3E4-g7rPTK220FEKXZCQ_oEbKYP3KNJHRXMw2fWjxj6KRD3LYnl-js=s1600-w800"
            ],
            "name": "CÔNG VIÊN GIA ĐỊNH",
            "category": "Entertainment",
            "address": {
                "position": {
                    "lat": 10.8132439,
                    "lng": 106.6759091
                },
                "label": "Phường 3, Gò Vấp, Ho Chi Minh City 70000, Vietnam"
            },
            "startDate": "2024-03-04T00:00:00.000Z",
            "startTime": "09:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJ2zxD0WkpdTER6N1xbSp0LBY",
            "purchaseLink": ""
        }
    ],
"""

TRANSPORT_MODULE = TECHNICAL_CONTEXT + """\nTRANSPORT MODULE:
    Transport modules are added primarily in a few ways. The first way is at the start and the end of the trip in the form of a pickup and dropoff from and to the airport. Please take note that this a common case. When planning from new trips, take note of this point and include it in new trips. Another main area where transportation is required when a customer is travelling across multiple cities throughout the holiday. Transport module is required when transferring between one city to another city, this can be either at the start of the day or at the end of the day when transiting between cities. You will learn of this in the various examples that we show later. 

    EXAMPLE JSON FORMAT FOR TRANSPORT MODULE:
    -------------------------------
    "transportations": [
            {
                "images": [],
                "name": "Private airport pickup",
                "type": "Van",
                "arrivalLocation": {
                    "position": {
                        "lat": 10.7756,
                        "lng": 106.7019
                    },
                    "label": "Ho Chi Minh City, Ho Chi Minh, Vietnam"
                },
                "startDate": "2024-02-27T00:00:00.000Z",
                "startTime": "07:00",
                "duration": 60
            },]


    AN EXAMPLE COULD BE LIKE THIS FOR A SPECIFIC NUMBER OF DAYS
 "transportations": [
        {
            "images": [],
            "name": "Private airport pickup",
            "type": "Van",
            "arrivalLocation": {
                "position": {
                    "lat": 10.7756,
                    "lng": 106.7019
                },
                "label": "Ho Chi Minh City, Ho Chi Minh, Vietnam"
            },
            "startDate": "2024-02-27T00:00:00.000Z",
            "startTime": "07:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "purchaseLink": ""
        },
        {
            "images": [],
            "name": "Private airport dropoff",
            "type": "Van",
            "arrivalLocation": {
                "position": {
                    "lat": 10.7756,
                    "lng": 106.7019
                },
                "label": "Ho Chi Minh City, Ho Chi Minh, Vietnam"
            },
            "startDate": "2024-03-04T00:00:00.000Z",
            "startTime": "10:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "purchaseLink": ""
        }
    ],
"""

EXPERIENCE_MODULE = TECHNICAL_CONTEXT + """\nEXPERIENCE MODULE:
    Experience modules are specific parts of an itinerary which are to be paid by the customer and can be a group of multiple activities done at one go. For example an experience could be a walking tour of Hanoi City which involves 6-8 different places at one go. As such, an experience is assigned to multiple places in each module to make sure that when creating an itinerary, the itinerary does not repeat the same activity module if its covered in an experience. Please take note of that. More importantly, the biggest types of experiences can be a day trip from a specific city. In order to understand if a specific experience is a day trip from City X, you can decipher this from looking at the accommodations address for that night where the locals are staying. If an experience is 7 hours or longer, it can be the only experience for that day. Please take note of that it should be the only experience for that day as it will take up too much time of the day and the client will not be able to do another experience. You can put another activity or food & beverage as dinner in the remaining parts of the day

    EXAMPLE JSON FORMAT FOR EXPERIENCE MODULE:
    -------------------------------
    "experiences": [
                {
                "name": "Saigon Princess Dining Cruise in Ho Chi Minh City",
                "category": "Cruises",
                "address": {
                    "position": {
                        "lat": 10.7674698,
                        "lng": 106.707975
                    },
                    "label": "Saigon Princess - Unique Luxurious Dining Cruise, SAIGON PORT, 05 Nguyễn Tất Thành, Phường 12, Quận 4, Thành phố Hồ Chí Minh 700000, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "19:30",
                "duration": 120,
                "placeId": ""
                }]


    AN EXAMPLE COULD BE LIKE THIS FOR A SPECIFIC NUMBER OF DAYS
"""

FOOD_MODULE = TECHNICAL_CONTEXT + """\nFOOD MODULE:
    Food & Beverages as part of other itineraries are usually top eating and drinking spots. These are recommendations as carefully placed into a specific part of the itinerary so when recommending them as part of an itinerary, please take note of the time of day and the location of the food & beverage

    EXAMPLE JSON FORMAT FOR FOOD MODULE:
    -------------------------------
    "foodPlaces": [
            {
                "name": "Ngon Restaurant",
                "address": {
                    "position": {
                        "lat": 10.7774178,
                        "lng": 106.6996655
                    },
                    "label": "160 Pasteur, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
                },
                "startDate": "2024-02-29T00:00:00.000Z",
                "startTime": "10:00",
                "duration": 60
                "placeId": "ChIJoz2M2EgvdTERLFRcCOtuC70"
            }
        ],



    AN EXAMPLE COULD BE LIKE THIS FOR A SPECIFIC NUMBER OF DAYS
    "foodPlaces": [
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANJU3DtQNth8YY4IGF-02pfu7Ey0kbOXQQVH9xi5qpBhfdyVo70NABIBWCcFWiq3OXT2cg-t-skpY8QKPFyBPaqVCMSGghmMcmaGuso=s1600-w800"
            ],
            "name": "Ngon Restaurant",
            "address": {
                "position": {
                    "lat": 10.7774178,
                    "lng": 106.6996655
                },
                "label": "160 Pasteur, Bến Nghé, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
            },
            "startDate": "2024-02-29T00:00:00.000Z",
            "startTime": "10:00",
            "duration": 60,
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJoz2M2EgvdTERLFRcCOtuC70",
            "purchaseLink": ""
        }
    ],
"""

ACCOMMODATION_MODULE = TECHNICAL_CONTEXT + """\nACCOMMODATION MODULE:
    When putting in accommodations for a specific trip, do take note that every city needs to have a check in and check out day which reflects the time and day which the traveller will arrive in that city. Based on the itineraries presented and shared later, you willl have an idea which accommodations to present and populate. 

    EXAMPLE JSON FORMAT FOR ACCOMMODATION MODULE:
    -------------------------------
    "accommodations": [
            {
                "name": "Cherry Hotel and Apartment",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 10.8026367,
                        "lng": 106.6439211
                    },
                    "label": "406/14 Đ. Cộng Hòa, Phường 13, Tân Bình, Thành phố Hồ Chí Minh, Vietnam"
                },
                "checkInDate": "2024-02-27T00:00:00.000Z",
                "checkInTime": "11:00",
                "checkOutDate": "2024-03-04T00:00:00.000Z",
                "checkOutTime": "12:00",
                "placeId": "ChIJI8jlq2UpdTER-H7WsRMz43g",
                "purchaseLink": ""
            }]



    An EXAMPLE COULD BE LIKE THIS FOR A SPECIFIC NUMBER OF DAYS
    "accommodations": [
        {
            "images": [
                "https://lh3.googleusercontent.com/places/ANXAkqFU3pBnp8uIqJ1ONjoApO_qHUzktk6hs4qu4y7gf69nW9YeGYhcN7ekEmu2IKjD80o2hBFxbj8ND8Mi5hXnS2-IBEgzRoHjCBM=s1600-w800"
            ],
            "name": "Cherry Hotel and Apartment",
            "startRating": 5,
            "address": {
                "position": {
                    "lat": 10.8026367,
                    "lng": 106.6439211
                },
                "label": "406/14 Đ. Cộng Hòa, Phường 13, Tân Bình, Thành phố Hồ Chí Minh, Vietnam"
            },
            "checkInDate": "2024-02-27T00:00:00.000Z",
            "checkInTime": "11:00",
            "checkOutDate": "2024-03-04T00:00:00.000Z",
            "checkOutTime": "12:00",
            "cost": 0,
            "currency": "USD",
            "note": "",
            "rating": 5,
            "visit": 0,
            "placeId": "ChIJI8jlq2UpdTER-H7WsRMz43g",
            "purchaseLink": ""
        }
    ],
"""

EXAMPLES = """\nEXAMPLES:
    -------------------------------------------------------------------
    {
        "id": "65b8af26dafb30b3cb971115",
        "title": "7 days itinerary to Northern and Southern Vietnam",
        "startDate": "2024-02-28T00:00:00.000Z",
        "endDate": "2024-03-05T00:00:00.000Z",
        "departurePoint": {
            "pickup": {
                "startTime": "09:00",
                "description": "Private driver will receive you at the airport arrival hall after you exit the immigration center"
            },
            "meetup": null,
            "departureDate": "2024-02-28T00:00:00.000Z"
        },
        "returnPoint": {
            "returnDate": "2024-03-05T00:00:00.000Z",
            "startTime": "09:00",
            "description": "Driver will pick you up at the airport and drop you off 2 hours before your departure"
        },
        "routes": [
            {
                "city": "Da Nang",
                "country": "Vietnam",
                "label": "Da Nang, Vietnam",
                "position": {
                    "lat": 16.0748,
                    "lng": 108.224
                }
            },
            {
                "city": "Ho Chi Minh City",
                "country": "Vietnam",
                "label": "Ho Chi Minh City, Ho Chi Minh, Vietnam",
                "position": {
                    "lat": 10.7756,
                    "lng": 106.7019
                }
            }
        ],
        "days": [
            {
                "color": "#1C2B4B",
                "index": 1,
                "title": "Arrival in Hanoi and local exploration",
                "startAt": "2024-02-28T00:00:00.000Z",
                "endAt": "2024-02-28T23:59:59.000Z"
            },
            {
                "color": "#E5634B",
                "index": 2,
                "title": "Ninh Binh Day Tri",
                "startAt": "2024-02-29T00:00:00.000Z",
                "endAt": "2024-02-29T23:59:59.000Z"
            },
            {
                "color": "#3E3D87",
                "index": 3,
                "title": "Hoi An Exploration + Award Winning Memories Show ",
                "startAt": "2024-03-01T00:00:00.000Z",
                "endAt": "2024-03-01T23:59:59.000Z"
            },
            {
                "color": "#E09E4F",
                "index": 4,
                "title": "Day Trip to Hue + free time to enjoy Hoi An",
                "startAt": "2024-03-02T00:00:00.000Z",
                "endAt": "2024-03-02T23:59:59.000Z"
            },
            {
                "color": "#3569C0",
                "index": 5,
                "title": "Flight to Ho Chi Minh + Shopping time ",
                "startAt": "2024-03-03T00:00:00.000Z",
                "endAt": "2024-03-03T23:59:59.000Z"
            {
                "color": "#F28602",
                "index": 6,
                "title": "Full day Cu-Chi Tunnels Tour",
                "startAt": "2024-03-04T00:00:00.000Z",
                "endAt": "2024-03-04T23:59:59.000Z"
            },
            {
                "color": "#2F6C87",
                "index": 7,
                "title": "Home Sweet Home :)",
                "startAt": "2024-03-05T00:00:00.000Z",
                "endAt": "2024-03-05T23:59:59.000Z"
            }
        ],
        "status": "PUBLISHED",
        "author": {
            "id": "653381bbf456012ca2948993",
            "fullname": "Holicay",
            "username": "admin.ho",
            "email": "admin@holicay.com"
        },
        "activities": [
            {
                "name": "Full Day Cu Chi Tunnel Tour",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 11.1426821,
                        "lng": 106.4623106
                    },
                    "label": "Cu Chi Tunnel, Phú Hiệp, Phú Mỹ Hưng, Củ Chi, Ho Chi Minh City, Vietnam"
                },
                "startDate": "2024-03-04T00:00:00.000Z",
                "startTime": "07:00",
                "duration": 480,
                "activityId": "activityId_0"
            },
            {
                "name": "Hanoi Street Food tour and landmark exploration",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 21.034059,
                        "lng": 105.8506368
                    },
                    "label": "Hanoi Old Quarter, Phố Hàng Ngang, Old Quarter, Hàng Đào, Hoàn Kiếm, Hanoi, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "12:30",
                "duration": 240,
                "activityId": "activityId_1"
            },
            {
                "name": "Free time to explore Hanoi River and Central Walking Street",
                "category": "Other",
                "address": {
                    "position": {
                        "lat": 21.0286669,
                        "lng": 105.8521484
                    },
                    "label": "Hoàn Kiếm Lake, Hang Trong, Hoàn Kiếm, Hanoi, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "16:30",
                "duration": 150,
                "activityId": "activityId_2"
            },
            {
                "name": "Full Day Ninh Binh Tour",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 20.2660773,
                        "lng": 105.9699457
                    },
                    "label": "Tràng An, Đông Thành, Ninh Bình, Vietnam"
                },
                "startDate": "2024-02-29T00:00:00.000Z",
                "startTime": "07:00",
                "duration": 510,
                "activityId": "activityId_3"
            },
            {
                "name": "Cat Cat Village exploration",
                "category": "Shopping",
                "address": {
                    "position": {
                        "lat": 22.3301416,
                        "lng": 103.8324947
                    },
                    "label": "Cat Cat Village, San Sả Hồ, Sa Pa, Lao Cai, Vietnam"
                },
                "startDate": "2024-03-01T00:00:00.000Z",
                "startTime": "11:00",
                "duration": 210,
                "activityId": "activityId_4"
            },
            {
                "name": "Hmong Village Day Tour ",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 22.3184317,
                        "lng": 103.8490041
                    },
                    "label": "Hmong village homestay, San Sả Hồ, Sa Pa, Lao Cai, Vietnam"
                },
                "startDate": "2024-03-02T00:00:00.000Z",
                "startTime": "08:00",
                "duration": 390,
                "activityId": "activityId_5"
            }
        ],
        "foodPlaces": [
            {
                "name": "Dinner at Pizza 4P's Ben Thanh (reservations made for you)",
                "address": {
                    "position": {
                        "lat": 10.7733572,
                        "lng": 106.6976176
                    },
                    "label": "8 Thủ Khoa Huân, Phường Bến Thành, Quận 1, Thành phố Hồ Chí Minh 700000, Vietnam"
                },
                "startDate": "2024-03-04T00:00:00.000Z",
                "startTime": "19:00",
                "duration": 90,
                "placeId": "ChIJfYtYmHkvdTERhCNHqNTzQ48"
            },
            {
                "name": "Dinner at Cha Ca Thang Long",
                "address": {
                    "position": {
                        "lat": 21.0329384,
                        "lng": 105.8461536
                    },
                    "label": "6B P. Đường Thành, Cửa Đông, Hoàn Kiếm, Hà Nội 000084, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "19:00",
                "duration": 90,
                "placeId": "ChIJsT3Lwv6rNTERVkFxNHqo3JI"
            }
        ],
        "accommodations": [
            {
                "name": "Meliá Hanoi",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 21.024347,
                        "lng": 105.8486232
                    },
                    "label": "44 P. Lý Thường Kiệt, Trần Hưng Đạo, Hoàn Kiếm, Hà Nội, Vietnam"
                },
                "checkInDate": "2024-02-28T00:00:00.000Z",
                "checkInTime": "11:00",
                "checkOutDate": "2024-02-29T00:00:00.000Z",
                "checkOutTime": "06:45",
                "placeId": "ChIJ2ehlkZOrNTERzL1Vpx8rlfM"
            },
            {
                "name": "Pistachio Hotel Sapa",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 22.3347116,
                        "lng": 103.8387484
                    },
                    "label": "Số 29, Tổ 5 Đường Thác Bạc, TT. Sa Pa, Sa Pa, Lào Cai 661300, Vietnam"
                },
                "checkInDate": "2024-03-01T00:00:00.000Z",
                "checkInTime": "02:00",
                "checkOutDate": "2024-03-03T00:00:00.000Z",
                "checkOutTime": "07:00",
                "placeId": "ChIJewB5t25BzTYR4sYxgfMipSE"
            }
        ],
        "transportations": [
            {
                "name": "Private overnight transfer to Sa Pa",
                "type": "Van",
                "arrivalLocation": {
                    "position": {
                        "lat": 22.3347116,
                        "lng": 103.8387484
                    },
                    "label": "Pistachio Hotel Sapa, Thác Bạc, Sa Pa, Lao Cai, Vietnam"
                },
                "startDate": "2024-02-29T00:00:00.000Z",
                "startTime": "21:00",
                "duration": 360
            },
            {
                "name": "Private transfer back to Hanoi",
                "type": "Van",
                "arrivalLocation": {
                    "position": {
                        "lat": 21.2187149,
                        "lng": 105.8041709
                    },
                    "label": "Noi Bai International Airport (HAN) (HAN), Sóc Sơn, Hanoi, Vietnam"
                },
                "startDate": "2024-03-03T00:00:00.000Z",
                "startTime": "07:30",
                "duration": 390
            },
            {
                "name": "Flight from Hanoi to Ho Chi Minh City",
                "type": "Flight",
                "arrivalLocation": {
                    "position": {
                        "lat": 10.8184631,
                        "lng": 106.6588245
                    },
                    "label": "Tan Son Nhat International Airport (SGN), Truong Son Street, Tân Bình, Ho Chi Minh City, Vietnam"
                },
                "startDate": "2024-03-03T00:00:00.000Z",
                "startTime": "14:00",
                "duration": 60
            }
        ],
        "share": [
            {
                "mode": "share-with-members",
                "link": "c9s01a",
                "members": [
                    {
                        "member": {
                            "_id": "653381bbf456012ca2948993",
                            "email": "admin@holicay.com",
                            "fullname": "Holicay",
                            "username": "admin.ho",
                            "image": "https://api.holicay.com/uploads/Square_850585f7a6.png",
                            "id": "653381bbf456012ca2948993"
                        },
                        "email": null,
                        "role": "OWNER"
                    }
                ],
                "role": "VIEWER"
            },
            {
                "mode": "get-link",
                "link": "c9s01a",
                "members": [],
                "role": "VIEWER"
            }
        ],
        "currentAccessRole": "OWNER",
        "slug": "7-days-itinerary-to-northern-and-southern-vietnam-ouk0og",
        "experiences": []
    }
    -------------------------------------------------------------------
    {
        "id": "65b8c057dafb30b3cb973df2",
        "title": "7 days to Ha Long, Ninh Binh and Ho Chi Minh City",
        "startDate": "2024-02-28T00:00:00.000Z",
        "endDate": "2024-03-05T00:00:00.000Z",
        "departurePoint": {
            "pickup": {
                "startTime": "09:00",
                "description": "Private driver will receive you at the airport arrival hall after you exit the immigration center"
            },
            "meetup": null,
            "departureDate": "2024-02-28T00:00:00.000Z"
        },
        "returnPoint": {
            "returnDate": "2024-03-05T00:00:00.000Z",
            "startTime": "09:00",
            "description": "Driver will pick you up at the airport and drop you off 2 hours before your departure"
        },
        "routes": [
            {
                "city": "Da Nang",
                "country": "Vietnam",
                "label": "Da Nang, Vietnam",
                "position": {
                    "lat": 16.0748,
                    "lng": 108.224
                }
            },
            {
                "city": "Ho Chi Minh City",
                "country": "Vietnam",
                "label": "Ho Chi Minh City, Ho Chi Minh, Vietnam",
                "position": {
                    "lat": 10.7756,
                    "lng": 106.7019
                }
            }
        ],
        "days": [
            {
                "color": "#1C2B4B",
                "index": 1,
                "title": "Arrival in Hanoi and local exploration",
                "startAt": "2024-02-28T00:00:00.000Z",
                "endAt": "2024-02-28T23:59:59.000Z"
            },
            {
                "color": "#E5634B",
                "index": 2,
                "title": "Ninh Binh Day Trip",
                "startAt": "2024-02-29T00:00:00.000Z",
                "endAt": "2024-02-29T23:59:59.000Z"
            },
            {
                "color": "#3E3D87",
                "index": 3,
                "title": "Hoi An Exploration + Award Winning Memories Show ",
                "startAt": "2024-03-01T00:00:00.000Z",
                "endAt": "2024-03-01T23:59:59.000Z"
            },
            {
                "color": "#E09E4F",
                "index": 4,
                "title": "Day Trip to Hue + free time to enjoy Hoi An",
                "startAt": "2024-03-02T00:00:00.000Z",
                "endAt": "2024-03-02T23:59:59.000Z"
            },
            {
                "color": "#3569C0",
                "index": 5,
                "title": "Flight to Ho Chi Minh + Shopping time ",
                "startAt": "2024-03-03T00:00:00.000Z",
                "endAt": "2024-03-03T23:59:59.000Z"
            },
            {
                "color": "#F28602",
                "index": 6,
                "title": "Full day Cu-Chi Tunnels Tour",
                "startAt": "2024-03-04T00:00:00.000Z",
                "endAt": "2024-03-04T23:59:59.000Z"
            },
            {
                "color": "#2F6C87",
                "index": 7,
                "title": "Home Sweet Home :)",
                "startAt": "2024-03-05T00:00:00.000Z",
                "endAt": "2024-03-05T23:59:59.000Z"
            }
        ],
        "status": "PUBLISHED",
        "author": {
            "id": "653381bbf456012ca2948993",
            "fullname": "Holicay",
            "username": "admin.ho",
            "email": "admin@holicay.com"
        },
        "activities": [
            {
                "name": "Full Day Cu Chi Tunnel Tour",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 11.1426821,
                        "lng": 106.4623106
                    },
                    "label": "Cu Chi Tunnel, Phú Hiệp, Phú Mỹ Hưng, Củ Chi, Ho Chi Minh City, Vietnam"
                },
                "startDate": "2024-03-04T00:00:00.000Z",
                "startTime": "07:00",
                "duration": 480,
                "activityId": "activityId-6"
            },
            {
                "name": "Hanoi Street Food tour and landmark exploration",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 21.034059,
                        "lng": 105.8506368
                    },
                    "label": "Hanoi Old Quarter, Phố Hàng Ngang, Old Quarter, Hàng Đào, Hoàn Kiếm, Hanoi, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "12:30",
                "duration": 240,
                "activityId": "activityId-7"
            },
            {
                "name": "Free time to explore Hanoi River and Central Walking Street",
                "category": "Other",
                "address": {
                    "position": {
                        "lat": 21.0286669,
                        "lng": 105.8521484
                    },
                    "label": "Hoàn Kiếm Lake, Hang Trong, Hoàn Kiếm, Hanoi, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "16:30",
                "duration": 150,
                "activityId": "activityId-8"
            },
            {
                "name": "Full Day Ninh Binh Tour",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 20.2660773,
                        "lng": 105.9699457
                    },
                    "label": "Tràng An, Đông Thành, Ninh Bình, Vietnam"
                },
                "startDate": "2024-02-29T00:00:00.000Z",
                "startTime": "07:00",
                "duration": 510,
                "activityId": "activityId-9"
            },
            {
                "name": "Watch at Water Puppet show at Thang Long Theatre",
                "category": "Landmarks",
                "address": {
                    "position": {
                        "lat": 21.0316826,
                        "lng": 105.8533466
                    },
                    "label": "57B P. Đinh Tiên Hoàng, Hàng Bạc, Hoàn Kiếm, Hà Nội, Vietnam"
                },
                "startDate": "2024-02-29T00:00:00.000Z",
                "startTime": "17:30",
                "duration": 90,
                "activityId": "activityId-10"
            },
            {
                "name": "Pottery workshop at Hanoi Pottery village",
                "category": "Culture and History",
                "address": {
                    "position": {
                        "lat": 20.9773791,
                        "lng": 105.9136226
                    },
                    "label": "Bát Tràng, Gia Lâm, Hanoi, Vietnam"
                },
                "startDate": "2024-03-02T00:00:00.000Z",
                "startTime": "15:30",
                "duration": 210,
                "activityId": "activityId-11"
            },
            {
                "name": "Sung Sot Cave Tour (Surprise cave) ",
                "category": "Landmarks",
                "address": {
                    "position": {
                        "lat": 20.84397869999999,
                        "lng": 107.0914838
                    },
                    "label": "Sung Sot Cave"
                },
                "startDate": "2024-03-01T00:00:00.000Z",
                "startTime": "13:00",
                "duration": 90,
                "activityId": "activityId-12"
            },
            {
                "name": "Vung Vieng Fishing Village Tour",
                "category": "Nature",
                "address": {
                    "position": {
                        "lat": 20.8387061,
                        "lng": 107.1649394
                    },
                    "label": "Vung Vieng Fishing Village, Thành phố Hạ Long, Quảng Ninh, Vietnam"
                },
                "startDate": "2024-03-01T00:00:00.000Z",
                "startTime": "16:00",
                "duration": 90,
                "activityId": "activityId-13"
            },
            {
                "name": "Free & Easy: Bui Vien Walking Street",
                "category": "Landmarks",
                "address": {
                    "position": {
                        "lat": 10.7674231,
                        "lng": 106.6939905
                    },
                    "label": "Đ. Bùi Viện, Phường Phạm Ngũ Lão, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
                },
                "startDate": "2024-03-03T00:00:00.000Z",
                "startTime": "19:00",
                "duration": 150,
                "activityId": "activityId-14"
            }
        ],
        "foodPlaces": [
            {
                "name": "Dinner at Pizza 4P's Ben Thanh (reservations made for you)",
                "address": {
                    "position": {
                        "lat": 10.7733572,
                        "lng": 106.6976176
                    },
                    "label": "8 Thủ Khoa Huân, Phường Bến Thành, Quận 1, Thành phố Hồ Chí Minh 700000, Vietnam"
                },
                "startDate": "2024-03-04T00:00:00.000Z",
                "startTime": "19:00",
                "duration": 90,
                "placeId": "ChIJfYtYmHkvdTERhCNHqNTzQ48"
            },
            {
                "name": "Dinner at Cha Ca Thang Long",
                "address": {
                    "position": {
                        "lat": 21.0329384,
                        "lng": 105.8461536
                    },
                    "label": "6B P. Đường Thành, Cửa Đông, Hoàn Kiếm, Hà Nội 000084, Vietnam"
                },
                "startDate": "2024-02-28T00:00:00.000Z",
                "startTime": "19:00",
                "duration": 90,
                "placeId": "ChIJsT3Lwv6rNTERVkFxNHqo3JI"
            }
        ],
        "accommodations": [
            {
                "name": "Meliá Hanoi",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 21.024347,
                        "lng": 105.8486232
                    },
                    "label": "44 P. Lý Thường Kiệt, Trần Hưng Đạo, Hoàn Kiếm, Hà Nội, Vietnam"
                },
                "checkInDate": "2024-02-28T00:00:00.000Z",
                "checkInTime": "11:00",
                "checkOutDate": "2024-03-01T00:00:00.000Z",
                "checkOutTime": "09:00",
                "placeId": "ChIJ2ehlkZOrNTERzL1Vpx8rlfM"
            },
            {
                "name": "4-Star Ha Long Bay 2D1N Cruise",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 20.9274495,
                        "lng": 106.9860384
                    },
                    "label": "Tuần Châu, Hạ Long, Quảng Ninh, Vietnam"
                },
                "checkInDate": "2024-03-01T00:00:00.000Z",
                "checkInTime": "11:00",
                "checkOutDate": "2024-03-02T00:00:00.000Z",
                "checkOutTime": "11:00",
                "placeId": null
            },
            {
                "name": "Media Central Hanoi Hotel",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 21.0342348,
                        "lng": 105.8513453
                    },
                    "label": "108 P. Hàng Bạc, Hàng Đào, Hoàn Kiếm, Hà Nội, Vietnam"
                },
                "checkInDate": "2024-03-02T00:00:00.000Z",
                "checkInTime": "13:00",
                "checkOutDate": "2024-03-03T00:00:00.000Z",
                "checkOutTime": "07:00",
                "placeId": "ChIJhyBpuV6rNTER0XjTJ7kHXbI"
            },
            {
                "name": "Felix Hotel",
                "startRating": 5,
                "address": {
                    "position": {
                        "lat": 10.7680405,
                        "lng": 106.6927711
                    },
                    "label": "219/8A Đ. Phạm Ngũ Lão, Phường Phạm Ngũ Lão, Quận 1, Thành phố Hồ Chí Minh, Vietnam"
                },
                "checkInDate": "2024-03-03T00:00:00.000Z",
                "checkInTime": "17:30",
                "checkOutDate": "2024-03-05T00:00:00.000Z",
                "checkOutTime": "09:00",
                "placeId": "ChIJR5l-6FIvdTERIaqlJZZ7qSQ"
            }
        ],
        "transportations": [
            {
                "name": "Private transfer back to Hanoi",
                "type": "Van",
                "arrivalLocation": {
                    "position": {
                        "lat": 21.2187149,
                        "lng": 105.8041709
                    },
                    "label": "Noi Bai International Airport (HAN) (HAN), Sóc Sơn, Hanoi, Vietnam"
                },
                "startDate": "2024-03-03T00:00:00.000Z",
                "startTime": "07:30",
                "duration": 390
            },
            {
                "name": "Flight from Hanoi to Ho Chi Minh City",
                "type": "Flight",
                "arrivalLocation": {
                    "position": {
                        "lat": 10.8184631,
                        "lng": 106.6588245
                    },
                    "label": "Tan Son Nhat International Airport (SGN), Truong Son Street, Tân Bình, Ho Chi Minh City, Vietnam"
                },
                "startDate": "2024-03-03T00:00:00.000Z",
                "startTime": "14:00",
                "duration": 60
            },
            {
                "name": "Transfer to Ha Long Bay from Hanoi",
                "type": "Van",
                "arrivalLocation": {
                    "position": {
                        "lat": 20.9274495,
                        "lng": 106.9860384
                    },
                    "label": "Tuần Châu, Hạ Long, Quảng Ninh, Vietnam"
                },
                "startDate": "2024-03-01T00:00:00.000Z",
                "startTime": "10:00",
                "duration": 90
            }
        ],
        "share": [
            {
                "mode": "share-with-members",
                "link": "8s0zhy",
                "members": [
                    {
                        "member": {
                            "_id": "653381bbf456012ca2948993",
                            "email": "admin@holicay.com",
                            "fullname": "Holicay",
                            "username": "admin.ho",
                            "image": "https://api.holicay.com/uploads/Square_850585f7a6.png",
                            "id": "653381bbf456012ca2948993"
                        },
                        "email": null,
                        "role": "OWNER"
                    }
                ],
                "role": "VIEWER"
            },
            {
                "mode": "get-link",
                "link": "8s0zhy",
                "members": [],
                "role": "VIEWER"
            }
        ],
        "currentAccessRole": "OWNER",
        "slug": "7-days-to-ha-long-ninh-binh-and-ho-chi-minh-city-cymns4",
         "experiences": [
        {
            "images": [
                "https://api-staging.holicay.com/uploads/saigon-princess-cruise-ho-chi-minh-city-1_a7257b8749.webp",
                "https://api-staging.holicay.com/uploads/saigon-princess-cruise-ho-chi-minh-city_cae15a9b72.webp",
                "https://api-staging.holicay.com/uploads/saigon-princess-cruise-ho-chi-minh-city-2_b8a829705a.webp"
            ],
            "name": "Saigon Princess Dining Cruise in Ho Chi Minh City",
            "category": "Cruises",
            "address": {
                "position": {
                    "lat": 10.7674698,
                    "lng": 106.707975
                },
                "label": ", , , Saigon Princess - Unique Luxurious Dining Cruise, SAIGON PORT, 05 Nguyễn Tất Thành, Phường 12, Quận 4, Thành phố Hồ Chí Minh 700000, Vietnam"
            },
            "startDate": "2024-02-28T00:00:00.000Z",
            "startTime": "19:30",
            "duration": 120,
            "cost": 29.9,
            "currency": "USD",
            "note": "",
            "description": "Share a memorable night with your friends or family, and hop on this Saigon Princess cruise in Ho Chi Minh.\n\nHop on a luxury cruise ship and enjoy a 2-hour scenic ride across Saigon River overlooking the city’s skyline. \n\nHave the option to enjoy a delectable meal during your ride and devour a spread of local and international fares! \n\nBe serenaded by a live band throughout your journey for a truly romantic and unforgettable evening.",
            "placeId": "",
            "provider": "klook",
            "affiliateLink": ""
        }
    ]
    }
"""

GOLDEN_RULES = """
    FOLLOW THESE 
    Golden Rules of Travel Planning
    Before generating the final itinerary and learning all you have from the sample itineraries in the past section, there are some golden rules to follow when planning the trip. You MUST follow these rules before generating the entire itinerary as well. The rules are : 

    1) If a particular experience is 7 hours or longer, it can only be that specific experience for that day as the traveller will not have the time and energy to do anything else. So please take note of this when inputting a specific experience for that day based on your understanding from the past itineraries 
    2) A single day has only got 24 hours and the day usually starts at 8am. If the day starts at 8am, the day can only end by 11.59pm. Please take note of this context when planning the trip.
    3) When arriving into the very first city by plane, a pickup by van must be indicated. In the title of the transport module, the name of the airport must be mentioned somewhere. Use your knowledge to figure out which main airport of that city is.
    4) When leaving the last city and moving to the airport, a drop-off to the airport must be provided. In the title of the transport module, the name of the airport must be mentioned somewhere. Use your knowledge to figure out which main airport of that city is.
    5) There should only be a maximum of 3 recommendations of food & beverages in a day. One recommendation can be between 8am to 11am which is breakfast. The other recommendation is between 11am to 2pm which is for lunch. The other recommendation is between 5pm to 9pm which is for dinner. Please take note of what the sample itinerary had recommendation. Most breakfasts are provided by hotels anyway 
    6) When transiting from one city to another city, based on your understanding from the sample itineraries, there must be a transport module in place to showcase the transport between the two cities at an appropriate time. The duration should also be reflected in the module and the type of transport. Sometimes a domestic flight is needed while at times, simply a van or bus transfer is needed. You need to be specific when printing the json format. 
    7) The total number of activities, experiences, food & beverage, accommodations and transport module differs from itinerary to itinerary. You need to make sure that they make sense and not blindly copy from other itineraries. It needs to make sense for a person travelling. 
    8) You must print out and generate all the parameters for each module as listed in the section when being taught on the different modules 
    9) You must plan all the days of the entire itinerary out and not just plan the first day. If you did not plan out all the days required by the user, you have failed and you cannot fail in your mission. 
    10) You can only use the modules provided in the sample itineraries and not generate your own modules. As such, you are limited by the type of activities, food & beverages, accomodations and experiences and transport provided and listed in the sample itineraries. You are limited to that dataset provided only. 
    11) When printing out the trip itinerary in JSON format, it needs to follow the exact same format as per the sample itineraries that you have learned from. The format and structure is as such in an example itinerary which is a 7 days Trip in Ho Chi Minh. This is only an example of the format and structure of what the output should consist of.  Do not blindly copy the exact same itinerary : 

    """