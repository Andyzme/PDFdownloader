# PDFdownloader

# Installation

1. Get Docker

2. Run the commands on terminal/powershell:
    `docker-compose build && docker-compose up -d database && docker-compose up webapp`

3. To stop, press ctrl+c

4. To remove and stop all running docker containers:
    `docker stop $(docker ps -a -q) && docker system prune -a`
