# mtg-nginx-django-react
This is a full stack dockerized app to fetch Magic the Gathering card prices from Canadian sources.
The application is deployed using AWS EC2 and uses nginx.

# API
A simple django api that uses beautifulsoup4 to scrape Canadian websites for
Magic the Gathering card prices. 

Websites supported:
- kanatacg.com
- gauntletgamesvictoria.com
- houseofcards.ca

## API Usage
### REQUEST
`[GET] http://localhost:8080/?name=fblthp`

### RESPONSE
```json
{
  "House of Cards": [
    {
      "name": "Fblthp, the Lost ",
      "link": "https://houseofcards.ca/products/fblthp-the-lost-war-of-the-spark?_pos=1&_sid=8defefed9&_ss=r",
      "image": "https://cdn.shopify.com/s/files/1/0567/4178/9882/products/9b264e4e-460a-566d-9e33-623a96657a61_large.jpg?v=1635646962",
      "set": "War of the Spark",
      "stock": [
        [
          "NM",
          0.7
        ]
      ]
    },
    {
      "name": "Fblthp, the Lost (Timeshifted) ",
      "link": "https://houseofcards.ca/products/fblthp-the-lost-timeshifted-time-spiral-remastered?_pos=2&_sid=8defefed9&_ss=r",
      "image": "https://cdn.shopify.com/s/files/1/0567/4178/9882/products/a9f4408d-5682-5701-96e8-8a7106385e2a_37c4e076-eab0-4527-a3a9-6faa91e7bff5_large.jpg?v=1635652469",
      "set": "Time Spiral Remastered",
      "stock": [
        [
          "NM",
          0.9
        ],
        [
          "NM",
          12.3
        ]
      ]
    },
   
  ],
  "Gauntlet Games": [
    {
      "name": "Fblthp, the Lost",
      "link": "https://www.gauntletgamesvictoria.ca/catalog/magic_singles-time_spiral_remastered/fblthp_the_lost/1597931",
      "image": "https://crystal-cdn1.crystalcommerce.com/photos/6626182/medium/en_ItgBEahkLI.png",
      "set": "Time Spiral Remastered",
      "stock": [
        [
          "NM",
          0.99
        ]
      ]
    },
  ],
  "Wizards Tower": [
    {
      "name": "Fblthp, the Lost - Foil",
      "link": "https://www.kanatacg.com/catalog/magic_singles-time_spiral_remastered/fblthp_the_lost__foil/496491",
      "image": "http://cc-client-assets.s3.amazonaws.com/photo/kanatacg/file/faa7878dc7b449de9edd6691c45696c3/large/en_ItgBEahkLI.png",
      "set": "Time Spiral: Remastered",
      "stock": [
        [
          "NM",
          18
        ]
      ]
    },
  ]
}
```

# Frontend
The front end uses React and Material UI.

![image](https://user-images.githubusercontent.com/65413229/185690059-49449faa-18cb-4257-824d-be352985880d.png)

