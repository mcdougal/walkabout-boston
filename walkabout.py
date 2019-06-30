#!/usr/bin/env python

with open('walkabout.template.html') as f:
    html = f.read()

tiles = [
    ("front-door.jpg", "v", "4/27/13 at 5:59pm",
     "I began my walkabout at the front door of my apartment building in Mission Hill, right near Brigham Circle. I live in a nondescript, three story complex at the bottom of Wait Street. For the past three years I have lived off campus, and it has been interesting to see the different types of residences available. I grew up in rural Connecticut in a house where you couldn't see the neighbors from the front yard because there were too many trees in the way. In contrast, Boston is all about squeezing as many buildings as close together as possible."),
    ("apartments.jpg", "h", "4/27/13 at 1:49pm",
     "This is a chain of apartment buildings next to the Kevin W. Fitzgerald park in Mission Hill. It is a perfect example of Boston's tendency to cram buildings right up next to each other. When reflecting on the Boston community, I think this is an important aspect to consider. People are making their lives in a small, crowded area with so much hustle and bustle going on every day. Yet I am constantly surprised by the overwhelming kindness of the many Bostonians that I run into on a daily basis. Coming from a rural neighborhood, I can't imagine what it must be like to grow up in a city."),
    ("shoes.jpg", "v", "4/19/13 at 12:25pm",
     "Of course, kids will always find something to do. This photo was taken right outside my apartment building. If you walk up the street, you will find even more shoes on the power lines. If you take a left onto Pequot Street, you'll find even more shoes! I often hear kids playing outside my window, and I am guessing they are the culprits. But I am curious who is so unlucky as to have their shoes thrown onto power lines. I hope it is not all the same person!"),
    ("stores.jpg", "v", "4/27/13 at 11:41am",
     "There are many aspects of Boston that are very similar to my hometown in Connecticut. This is a photo of the shopping plaza right down the street. It has a Stop and Shop, a Wallgreens, and a TGI Fridays. I have only ever lived in Boston and Connecticut, and I have never really traveled outside the Northeast, but I imagine that no matter where you go in the country you will find a plaza just like this one. It is fascinating how the geographical expansion of businesses has created a baseline of cultural similarities within our nation. This helps explain our development as a culture of consumers. When you can find a McDonald's on every street corner in every city, it is no surprise that consumerism has become a fundamental aspect of our culture. I am not trying to cast a negative light on this fact, however. We are fortunate to live in a nation with such a high standard of living and easy access to all the necessities of life."),
    ("snake.jpg", "h", "4/19/13 at 12:34pm",
     "One thing I miss about my hometown is its abundance of nature. There were at least three wonderful parks within walking distance of my home. In Boston, nature is a lot harder to find. There is the Fens, the Arboretum, the Boston Common, and a few other parks, but nothing really compares unless you have a car and can travel outside the city to a place like the Fells. This is why I am so delighted to run into little hints of nature within the city. This is a photo of a snake I found next to the staircase that leads up to the  Kevin W. Fitzgerald park. I find it amazing that a city can harbor life such as this, and it makes me wonder what other creatures I might see if I just keep my eyes open."),
    ("calumet.jpg", "h", "4/20/13 at 3:09pm",
     "This photo was taken at the bottom of Calumet Street at the Brigham Circle intersection. One unique aspect I have noticed about Boston is the way its streets are laid out. Boston has developed gradually as a city over hundreds of years. As a result, its streets have grown organically over time. This has led to crooked one-ways and confusing intersections. Brigham Circle is a prime example of this, with five streets joining together in a complex flow of traffic."),
    ("graffiti-1.jpg", "v", "4/20/13 at 3:13pm",
     "Every city is bound to have its share of graffiti artists. Boston is no different. However, graffiti is especially common in the Mission Hill area because it is right next to the Massachusetts College of Art and Design. I doubt that every piece of graffiti was done by MassArt students, but I bet that they are major contributors. This photo depicts an interesting piece done at the top of a cliff that falls away from the Kevin W. Fitzgerald park. Personally, I think that tasteful graffiti makes an area more interesting and provides insight into the culture."),
    ("graffiti-2.jpg", "v", "4/20/13 at 3:13pm",
     "This is a photo of a graffiti heart that is on the wall next to a shop on Tremont Street, by the Mission Church."),
    ("graffiti-3.jpg", "v", "4/20/13 at 3:14pm",
     "This photo is also on the wall of a building on Tremont Street by the Mission Church. A student that goes to MassArt told me she has seen this in one of the MassArt academic buildings."),
    ("school-art-wall.jpg", "h", "4/20/13 at 3:20pm",
     "Illegal graffiti art is prevalent in Boston, but so are sanctioned murals. This is a photo of a school right near the Mission Church. I think it is wonderful that such a creative design was painted on the wall of a school. My elementary school in Connecticut did not have anything like this. In fact, there were very few murals in my hometown and the surrounding area. In contrast, Boston has so many!"),
    ("mission-church.jpg", "h", "4/20/13 at 3:16pm",
     "Every city will also have its share of churches representing all religions and all denominations. This is a photo of the Mission Church, a Roman Catholic church. It is an iconic building in the Mission Hill area. It sits at the top of a hill and its spires can be spotted all the way from the Boston Police Station, and possibly even further. As I write this, its bells are tolling the hour."),
    ("sociedad-latina.jpg", "h", "4/20/13 at 3:23pm",
     "One difference between Boston and my hometown is that Boston is very diverse. This is a photo of the Sociedad Latina office in Mission Hill on Tremont Street. I am thrilled about the mix of cultures in the Mission Hill area, and in Boston in general. I feel like I grew up in such a silo, and this is a great first step out of that. I have been inspired to take an even bigger step after I graduate and travel to South America to see what cultures are like outside of this country. We live in a culturally rich world, and I am excited to learn even more about it."),
    ("connors-center.jpg", "h", "4/27/13 at 3:15pm",
     "It is interesting how different areas of Boston have developed different defining characteristics. This is a photo of the Connors Center, a part of Brigham and Women's Hospital, one of the many hospitals in the Longwood area."),
    ("brigham-and-womens.jpg", "h", "4/27/13 at 3:17pm",
     "This is a photo of another building that is part of Brigham and Women's."),
    ("dana-farber.jpg", "v", "4/27/13 at 3:21pm",
     "The Dana-Farber Cancer Institute is also in the Longwood area."),
    ("hospitals-sign.jpg", "h", "4/27/13 at 3:22pm",
     "So is Beth Israel Deaconess and the Children's Hospital. I am curious as to why this area became so profuse with hospitals and health centers. Is it beneficial to have them all next to each other? It seems to me like it would be more useful to have them spread throughout the city. There are definitely a lot more hospitals in the Boston area than there are in my hometown. There is also a lot more research. I would label Boston and Cambridge as hubs of health-related research. This is especially true considering the number of colleges and universities in the area, because professors in higher-education schools often do research at the forefront of their fields."),
    ("fenway-park.jpg", "v", "4/27/13 at 3:41pm",
     "In the United States, sports are always a core part of a city's culture. My walkabout happened to take place during baseball season, and the area around Fenway Park was pretty crowded. This picture was taken a few hours before a Red Sox game was going to start. I am ashamed to admit it, but I have still not gone to a Red Sox game, even though I have lived in this city for five years. It is funny how you can live in a place for so long and never take part in its most culturally fundamental events. Fortunately, I will be working in the area after I graduate, so I haven't lost my chance yet. This walkabout reminded me that I should really take advantage of these opportunities while I am still here."),
    ("citgo.jpg", "v", "4/27/13 at 3:45pm",
     """This is a photo of the iconic Citgo sign taken from next to Fenway Park. A friend once told me a funny story about how she was trying to find someone, and she asked "what do you see?" The person responded, "I see a giant Citgo sign," and my friend said "that doesn't help, you can see that sign from everywhere in the city!" According to <a href="http://en.wikipedia.org/wiki/Citgo#The_Boston_Citgo_sign">Wikipedia</a>, the current version of the sign was unveiled in 2005, but the original was built in 1940. Five years in Boston have helped me come to appreciate the city's quirky history and entertaining landmarks."""),
    ("pru.jpg", "v", "4/27/13 at 4:31pm",
     "Another iconic structure in Boston is the Prudential Center. Every illustration of the Boston skyline is punctuated by this building. Since it is right next to the Northeastern campus, it has always been my guiding star. I know that no matter where I am in the city, I just have to head towards the Pru to find my way home."),
    ("christian-science-center.jpg", "v", "4/27/13 at 4:41pm",
     "Northeastern is incredibly fortunate to be located in such a cultural and artistic hub within Boston. Aside from being next to the Prudential Center, it is also right next to the Christian Science Center. I find this building to be one of the most beautiful in all of Boston. Its architecture is so grand and complex. It is a refreshing break from the steel monoliths that dominate the skyline."),
    ("reflecting-pool.jpg", "h", "4/27/13 at 4:41pm",
     "The reflecting pool is another of my favorite Boston structures. I have spent countless days and nights sitting by its side, reflecting on the incredible feats of engineering and science that were required to bring this city to life. There is something about this large sheet of water mirroring the cities structural accomplishments that makes one feel awed by our capabilities as human beings."),
    ("symphony-hall.jpg", "h", "4/27/13 at 4:29pm",
     "Symphony Hall is another iconic building near Northeastern. This building is a mark of the city's musical culture. Attending a concert at Symphony Hall is another thing on my Boston bucket list. I really should have visited by now, considering I did a presentation on it in my Introduction to Music class Freshman year."),
    ("mfa.jpg", "h", "4/27/13 at 4:12pm",
     "In the other direction from Symphony Hall there is the Museum of Fine Arts. This is a wonderful museum, and I appreciate that Northeastern students can get in for free. I particularly like the new contemporary art wing. My favorite exhibit was probably the Chihuly glass exhibit they had a while back."),
    ("baby-head.jpg", "v", "4/27/13 at 4:13pm",
     "Of course, one cannot take pictures of the MFA without taking a picture of the baby heads."),
    ("fens-bridge.jpg", "h", "4/27/13 at 3:53pm",
     "The closest thing to my hometown in Boston is probably the Fens. It provides a refreshing escape from the drab metal and concrete of the city. I think it is important for every city to have parks where its residents can go for some peace and quiet. City life can get very stressful with the pressure of deadlines, crowded public transportation, and constant noise."),
    ("community-garden.jpg", "v", "4/27/13 at 3:57pm",
     "The Fens also serves as an area for the community to congregate. This is a photo of a garden in the community gardens section of the Fens. This reminds me a lot of my hometown because there are a lot of gardens there, and there is a large gardening community. Gardening is a great way to bring people together because it allows them to cultivate living things and provide beauty to the city."),
    ("rose-garden.jpg", "h", "4/27/13 at 4:07pm",
     "Another community gardening section of the Fens is the rose garden. The rose garden is such a pleasant place to walk through during the summer; it is walled in by tall hedges and the pleasant aroma of roses permeates the air. Unfortunately, there are not any roses at this time of year. This is a photo of a fountain that sits in the center of the garden."),
    ("rabbit.jpg", "h", "4/27/13 at 4:08pm",
     "Though I didn't see any roses, I did see a rabbit. This photo was taken in the rose garden by the statue in the back."),
    ("goose.jpg", "v", "4/27/13 at 4:00pm",
     "Geese are definitely a common trait of the northeast, always to be seen flying in V's or walking in parks. My hometown definitely has its share of geese. In my opinion, however, the Fens has way too many geese. They are surprisingly acclimated to humans, too. The goose in this picture walked within two feet of me as it went past, and probably would have walked into me if I hadn't stepped out of the way."),
    ("northeastern.jpg", "v", "4/27/13 at 4:22pm",
     "Boston is well known for being a college city. As might be expected, this is another difference between my hometown and Boston. There are a few colleges and universities in my area of Connecticut, but not very many. The majority of the population is made up of older working professionals with pre-college aged children. I feel very lucky to have gone to college in a city with so many other students. I can't imagine what it must be like to go to a college like the University of New Hampshire where the only students you ever interact are those in your school. I tried to highlight Boston's abundance of schools on my walkabout, so I took pictures at Northeastern..."),
    ("emmanuel.jpg", "v", "4/27/13 at 3:31pm",
     "...and Emmanuel"),
    ("berklee.jpg", "v", "4/27/13 at 4:47pm",
     "...and Berklee"),
    ("wentworth.jpg", "v", "4/27/13 at 5:45pm",
     "...and Wentworth"),
    ("massart.jpg", "v", "4/27/13 at 5:48pm",
     '...and MassArt. And this is just a small fraction of the schools in the area. According to <a href="http://zipatlas.com/us/ma/boston/zip-code-comparison/percentage-college-students.htm">zipatlas.com</a>, over 50% of the population is college students in most of the Boston zip codes.'),
    ("boston.jpg", "h", "4/27/13 at 5:00pm",
     "I never really grasped how much Boston has to offer until I started walking around taking pictures and realized that it would take months to document every part of the city. It has been quite the change for me, moving from a small town in Connecticut with under 10,000 residents to a city in Massachusetts with over 600,000. But what I have come to realize is that there are so many cultural similarities injected throughout the Northeast. When it comes down to it, Boston is really not all that different from where I grew up; it is just a lot bigger. I am excited to call this city home for at least a few more years, but I hope that one day I can take my Boston experiences with me to other places in the world. No matter where I end up, however, Boston has already become the stepping stone to the rest of my life."),
    ]

tiles_html = ""
for photo, orientation, timestamp, description in tiles:
    tiles_html += """
  <div class="tile">
    <span class="timestamp">{timestamp}</span>
    <img class="photo photo-{orientation}" src="photos/{photo}"/>
    <span class="description">
      {description}
    </span>
  </div>
""".format(photo=photo, description=description, timestamp=timestamp, orientation=orientation)

    # <div class="modal">
    #   <div class="modal-frame">
    #     <span class="modal-close">X</span>
    #     <img class="modal-photo modal-photo-{orientation}" src="photos/{photo}"/>
    #   </div>
    # </div>

with open('walkabout.html','w') as f:
    f.write(html.format(tiles=tiles_html))
