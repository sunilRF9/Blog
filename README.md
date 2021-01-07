# Django blog - PostgreSQL + AWS + Redis 🚀

#### How?

- Minimalist Django Blog with `PostgreSQL` as the backend to store Blog posts, free tier of `ElephantSQL` is used which provides - PostgreSQL as a Service in the cloud.

- Caching is taken care by `Redis`. A free-tier on `Redis Labs` is used.

- `AWS S3` is used serve static files and store images from the Blog posts.

- Has a simple search feature.

- Has Basic and Session Authentication on the Detail API View. 

- The Blog is deployed on `Heroku`. 

- SSL/TLS certificates are added using `Cloudflare`. 

- Has a public facing API which can be accessed at `https://www.sunilbs.com/api/`

- Checkout the blog at [https://sunilbs.com](https://www.sunilbs.com)

#### Screenshots

- Homepage 

![2021-01-06_12:30:47](https://user-images.githubusercontent.com/45355098/103739087-1a44fd00-501b-11eb-8e6f-fa04ea7daabf.png)

- Blogs

![2021-01-06_12:33:57](https://user-images.githubusercontent.com/45355098/103739352-8162b180-501b-11eb-89a5-c7d4881a78a7.png)

- API 

![2021-01-06_12:32:30](https://user-images.githubusercontent.com/45355098/103739183-4496ba80-501b-11eb-9f31-f90d5cfe9f8c.png)
