#include <glut.h>
#include <stdlib.h>
#include <stdio.h>
 float x1=0;
 float y1=0;
 float x2=0;
 float y2=0;
 
 void drawWindow()
 {
     glClearColor(1.0f, 0.5f, 0.0f, 1.0f);
     glClear(GL_COLOR_BUFFER_BIT);
 
     glBegin(GL_LINES);
     glVertex2f(0,0);
     glVertex2f(0.300, 0);
     glEnd();

     glBegin(GL_LINES);
     glVertex2f(0,0);
     glVertex2f(0, 0.300);
     glEnd();
 
 glPointSize(3);
 
 	 glBegin(GL_POINTS);
	glVertex2f(x1, y1);
	glEnd();
     
      glBegin(GL_POINTS);
	glVertex2f(x2, y2);
	glEnd();
	
	glBegin(GL_LINES);
     glVertex2f(x1,y1);
     glVertex2f(x2, y2);
     glEnd();
     
     glFlush();
     
     
 }
 
 int main(int argc, char *argv[])
 {
    glutInit(&argc, argv);
    
    glutCreateWindow("Plotar uma reta entre os pontos A e B");
    printf("Digite a coodenada X do P1: ");
    scanf("%f", &x1);
    printf("Digite a coodenada Y do P1: ");
    scanf("%f", &y1);
    printf("Digite a coodenada X do P2: ");
    scanf("%f", &x2);
    printf("Digite a coodenada Y do P2: ");
    scanf("%f", &y2);
    
     x1=x1/1000;
 	 y1=y1/1000;
	 x2=x2/1000;
 	 y2=y2/1000;
    
   
    glutDisplayFunc(drawWindow);
    glutMainLoop();
   return 1;
 }

