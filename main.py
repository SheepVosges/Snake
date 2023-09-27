import sys, random
import pygame



class Game:

    def  __init__(self):
        
        self.ecran = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("Jeu Snake")
        self.jeu_encours = True

        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 10

        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        self.pomme = 10

        self.clock = pygame.time.Clock()

        self.positions_serpent = []
        self.taille_du_serpent = 1
        
        self.ecran_du_debut = True


        self.score = 0


    def creer_limite(self):
        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)
        
        pygame.draw.line(self.ecran,(255,255,255),(110,100),(110,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(120,100),(120,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(130,100),(130,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(140,100),(140,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(150,100),(150,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(160,100),(160,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(170,100),(170,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(180,100),(180,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(190,100),(190,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(200,100),(200,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(210,100),(210,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(220,100),(220,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(230,100),(230,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(240,100),(240,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(250,100),(250,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(260,100),(260,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(270,100),(270,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(280,100),(280,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(290,100),(290,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(300,100),(300,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(310,100),(310,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(320,100),(320,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(330,100),(330,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(340,100),(340,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(350,100),(350,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(360,100),(360,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(370,100),(370,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(380,100),(380,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(390,100),(390,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(400,100),(400,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(410,100),(410,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(420,100),(420,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(430,100),(430,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(440,100),(440,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(450,100),(450,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(460,100),(460,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(470,100),(470,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(480,100),(480,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(490,100),(490,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(500,100),(500,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(510,100),(510,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(520,100),(520,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(530,100),(530,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(540,100),(540,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(550,100),(550,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(560,100),(560,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(570,100),(570,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(580,100),(580,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(590,100),(590,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(600,100),(600,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(610,100),(610,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(620,100),(620,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(630,100),(630,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(640,100),(640,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(650,100),(650,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(660,100),(660,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(670,100),(670,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(680,100),(680,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(690,100),(690,600),1)
        pygame.draw.line(self.ecran,(255,255,255),(700,100),(700,600),1)
    
        pygame.draw.line(self.ecran,(255,255,255),(100,110),(700,110),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,120),(700,120),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,130),(700,130),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,140),(700,140),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,150),(700,150),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,160),(700,160),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,170),(700,170),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,180),(700,180),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,190),(700,190),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,200),(700,200),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,210),(700,210),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,220),(700,220),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,230),(700,230),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,240),(700,240),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,250),(700,250),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,260),(700,260),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,270),(700,270),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,280),(700,280),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,290),(700,290),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,300),(700,300),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,310),(700,310),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,320),(700,320),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,330),(700,330),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,340),(700,340),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,350),(700,350),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,360),(700,360),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,370),(700,370),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,380),(700,380),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,390),(700,390),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,400),(700,400),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,410),(700,410),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,420),(700,420),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,430),(700,430),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,440),(700,440),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,450),(700,450),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,460),(700,460),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,470),(700,470),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,480),(700,480),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,490),(700,490),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,500),(700,500),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,510),(700,510),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,520),(700,520),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,530),(700,530),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,540),(700,540),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,550),(700,550),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,560),(700,560),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,570),(700,570),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,580),(700,580),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,590),(700,590),1)
        pygame.draw.line(self.ecran,(255,255,255),(100,600),(700,600),1)


    def creer_les_messages(self, font ,message ,message_rectangle, couleur):

        if font == 'petite':
            font = pygame.font.SysFont("Lato",20,False)

        if font == 'moyenne':
            font = pygame.font.SysFont("Lato",30,False)

        if font == 'grande':
            font = pygame.font.SysFont("Lato",40,True)

        message = font.render(message,True,couleur)

        self.ecran.blit(message,message_rectangle)
    

    def start(self):
        
        while self.ecran_du_debut :
            
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN :
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_du_debut = False
                
            self.ecran.fill((0,0,0))
            self.creer_les_messages('grande','Snake',(350,300,100,50),(0,255,0))
            self.creer_les_messages('petite','Le But du jeu est que le serpent se développe',(250,200,200,5),(200,255,200))
            self.creer_les_messages('petite','Pour cela il a besoin de pommes ,mangez-en autant que que possible !!!',(190,220,200,5),(200,255,200))
            self.creer_les_messages('moyenne','Appuyer sur entrée pour commencer à jouer',(200,450,200,5),(100,255,100))
            


            pygame.display.flip()


        while self.jeu_encours :
            

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT :
                        if not self.serpent_direction_x == -10 :
                            self.serpent_direction_x = 10
                            self.serpent_direction_y = 0
                    
                    if evenement.key == pygame.K_LEFT :
                        if not self.serpent_direction_x == 10 :
                            self.serpent_direction_x = -10
                            self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN :
                        if not self.serpent_direction_y == -10 :
                            self.serpent_direction_x = 0
                            self.serpent_direction_y = 10

                    if evenement.key == pygame.K_UP :
                        if not self.serpent_direction_y == 10 :
                            self.serpent_direction_x = 0
                            self.serpent_direction_y = -10
 
                    
                    


            if self.serpent_position_x <= 100 or self.serpent_position_x >= 690 or self.serpent_position_y <= 100 or self.serpent_position_y >= 590: 
                sys.exit()


            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y

            if self.serpent_position_y == self.pomme_position_y and self.serpent_position_x == self.pomme_position_x:

                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)

                self.taille_du_serpent += 1
                self.score+= 1
            
            
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            self.positions_serpent.append(la_tete_du_serpent)

            if len(self.positions_serpent) > self.taille_du_serpent :
                self.positions_serpent.pop(0)

            self.ecran.fill((0,0,0))
        
            pygame.draw.rect(self.ecran,(100,100,100),(100,100,600,500),0)
            pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x,self.serpent_position_y,self.serpent_corps,self.serpent_corps))
            pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme,self.pomme))

            for partie_du_serpent in self.positions_serpent:
                pygame.draw.rect(self.ecran,(0,255,0),(partie_du_serpent[0],partie_du_serpent[1],self.serpent_corps,self.serpent_corps))

            for partie_du_serpent in self.positions_serpent[:-1]:

                if la_tete_du_serpent == partie_du_serpent:
                    
                    sys.exit()

            self.creer_les_messages('grande','Snake Game', (320,10,100,50), (255,255,255))
            self.creer_les_messages('grande','score : {}'.format(str(self.score)), (350,50,50,50), (255,255,255))

            self.creer_limite()
            self.clock.tick(15)

            pygame.display.flip()   



if __name__ == '__main__' :
    pygame.init()
    Game().start()
    pygame.QUIT()