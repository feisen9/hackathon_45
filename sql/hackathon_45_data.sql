use hackathon_45;


insert into `user`(id, username, pass, created_at,updated_at,icon) 
values(1,"admin",123456,"2000-01-01 0:00:00","2000-01-01 0:00:00", '70ffb0edf1be75b055c81b9e5ecd4362_610_525.jpg!ys.jpeg');

insert into `user`(id, username, pass, created_at, updated_at,icon) 
values(2,"feisen",123456,"2000-01-01 0:00:00","2000-01-01 0:00:00", 'R-C.d698027c45cb9d1523ead7faf14e1327.jpeg');

insert into content(id, title, summary, contenttype, numlike, numview, created_at, updated_at)
values(101, '选择之路：The Road Not Taken', '《未选择的道路》是罗伯特·弗罗斯特的著名诗作，通过描述面临两条分叉小路的选择，探讨了生活中做出决策和放弃的主题。诗人选择了不被人走过的路，这个选择使他发现了世界的美，揭示了选择与发现美的紧密联系。', 'article', 10, 20, (select now()), (select now()))
;
insert into article(id ,articlename, author, articleinfo, articlecontent)
values(
101,
"The Road Not Taken",
"Robert Frost",
"- 诗名:The Road Not Taken
- 作者:Robert Frost
- 出版时间:1916年 
- 主题:人生的选择与放弃
- 情节:诗人行走在黄色的树林中,面临两条分叉的小路,必须选择其一,但又为放弃的另一条路感到遗憾。最终选择了人迹较少的一条路。
- 表达的思想:人生中不可避免地要作出选择,但每个选择都意味着放弃其他的可能性。作出选择后,很难再回头。但是,作出的选择会对人生产生深远的影响。",
"Two roads diverged in a yellow wood,
And sorry I could not travel both  
And be one traveler, long I stood  
And looked down one as far as I could  
To where it bent in the undergrowth;
Then took the other, as just as fair,  
And having perhaps the better claim,  
Because it was grassy and wanted wear;  
Though as for that the passing there  
Had worn them really about the same,
And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.
I shall be telling this with a sigh
Somewhere ages and ages hence: 
Two roads diverged in a wood, and I—
I took the one less traveled by,  
And that has made all the difference.

诗意解析:
- 这是一首讲述人生选择题材的诗歌。诗人面对两条路,代表两种生活或选择方式,选择其一,但又为未选择的另一条路感到遗憾。
- 两条路在黄色的树林中分叉,象征人生中的重大抉择。诗人检视两条路,都想选择,但不可能同时选择两条路。
- 最终,诗人选择了人迹较少的一条路。但他知道,一旦选择了一条路,就难以再回头选择另一条路。所以他可能会在未来,为此叹息。
- 但是,选择人迹较少的路,给诗人带来的影响是巨大的。这最后一句点出了主题。
- 这首诗歌表达了人生中无法避免的选择和放弃,以及每次选择都会产生深远影响的主旨。
该诗的信息连贯,主题明确,通过两条分叉的小路隐喻了人生中重要的决定。作者表达了对无法实现的其他可能性的留恋之情。但最后也鼓励读者有勇气选择自己的路,并相信这将改变一生。
这首诗歌简短但意蕴深远,用一种很形象的比喻描绘了人生主题,是美国诗歌史上很重要的作品之一。其中表达的思想和内涵值得长期思考和醒悟。"
)
;
insert into content(title, summary, contenttype, numlike, numview, created_at, updated_at)
values('优美的文章22', 'summary of 优美的文章22', 'article', 0, 0,'2023-05-20 19:35:53','2023-05-20 19:35:53' )
;
insert into content(title, summary, contenttype, numlike, numview, created_at, updated_at)
values('优美的图书11', 'summary of 优美的图书11', 'book', 30, 40, (select now()), (select now()))
;
insert into content(title, summary, contenttype, numlike, numview, created_at, updated_at)
values('优美的照片11', 'summary of 优美的照片11', 'photo', 50, 60, (select now()), (select now()))
;

-- SELECT * FROM user;

-- select username, icon 
-- from user 
-- where username = 'feisen'
-- ;


-- select curdate();

-- select * 
-- from content c
-- where date(c.created_at) = curdate()
-- ;

-- select * 
-- from content c
-- where date(c.created_at) ='2023-05-21' 
-- ;

-- select id, title, summary, contenttype, numlike, numview from content where created_at = '2023-05-21' ;








