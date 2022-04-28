#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<netinet/in.h>
#include<string.h>
#include<unistd.h>

int main(int argc, char const *argv[])
{
  
   char buffer[1000];
   char msg[20];
  
   if(argc < 2){
   //server
      printf("Starting the server.\n");
       /*SOCKET CREATION*/
   struct sockaddr_in n;
   struct sockaddr_in m;
   socklen_t addr_size;
   int new_socket;
   int sockfd=socket(PF_INET,SOCK_STREAM,0);
   if(sockfd==-1)
   {
       printf("Socket creation error.\n");
       exit(1);
   }
  
   /*BIND*/
   n.sin_port=htons(8080);
   n.sin_addr.s_addr=INADDR_ANY;
   n.sin_family=AF_INET;
   int b=bind(sockfd,(struct sockaddr*)&n,sizeof(n));
   if(b==-1)
   {
       printf("Bind error.\n");
       exit(1);
   }
   printf("server IP:%s\n",inet_ntoa(n.sin_addr));
   if((listen(sockfd,1))==-1)
   {
       printf("Listen error.\n");
       exit(1);
   }
   addr_size=sizeof(m);
  
   if ((new_socket = accept(sockfd, (struct sockaddr *)&m, (socklen_t*)&addr_size))<0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }
   strcpy(msg,"pong");
   /*COMMUNICATON*/
   while(1)
   {
       read( new_socket , buffer, 1000);
    printf("%s\n",buffer );
    send(new_socket , msg , strlen(msg) , 0 );
   }
   close(sockfd);
   }
   else{
   //client
         int sock;
        struct sockaddr_in serv_addr;
        if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(atoi(argv[2]));
    if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr)<=0)
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }
    strcpy(msg,"ping");
    while(1)
    {
       send(sock , msg , strlen(msg) , 0 );   
           read( sock , buffer, 1000);
    printf("%s\n",buffer );
  
   }
  
   }
  

  
   return 0;
}