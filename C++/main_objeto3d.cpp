#include <glut.h>

GLfloat fAspect;

double rotate_y=0; 
double rotate_x=0;

// Função callback chamada para fazer o desenho
void Desenha(void)
{
	//  Limpa a tela e o Z-Buffer
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
	
	// Rotaciona quando o usuário muda rotate_x e rotate_y
 	glRotatef( rotate_x, 1.0, 0.0, 0.0 );
    glRotatef( rotate_y, 0.0, 1.0, 0.0 );
	
	// Desenha o cubo verde (wire-frame)
	glPushMatrix();
	glTranslatef(100,0,0);
	glColor3f(0.0f, 1.0f, 1.0f);
	glutWireCube(50.0f);
	glPopMatrix();
	

	// Desenha a esfera verde (wire-frame)
	glPushMatrix();
	glColor3f(0.0f, 1.0f, 0.0f);
	glutWireSphere(50, 50, 50);
	glPopMatrix();
	
	
	// Executa os comandos OpenGL
	glutSwapBuffers();
 }
 

// Função usada para especificar o volume de visualização
void EspecificaParametrosVisualizacao(void)
{
	// Especifica sistema de coordenadas de projeção
	glMatrixMode(GL_PROJECTION);
	// Inicializa sistema de coordenadas de projeção
	glLoadIdentity();

	// Especifica a projeção perspectiva
	gluPerspective(45,fAspect,0.1,500);

	// Especifica sistema de coordenadas do modelo
	glMatrixMode(GL_MODELVIEW);
	// Inicializa sistema de coordenadas do modelo
	glLoadIdentity();

	// Especifica posição do observador e do alvo
	gluLookAt(0,80,200, 0,0,0, 0,1,0);
}

// Função callback chamada quando o tamanho da janela é alterado 
void AlteraTamanhoJanela(GLsizei w, GLsizei h)
{
	// Para previnir uma divisão por zero
	if ( h == 0 ) h = 1;

	// Especifica o tamanho da viewport
	glViewport(0, 0, w, h);
 
	// Calcula a correção de aspecto
	fAspect = (GLfloat)w/(GLfloat)h;

	EspecificaParametrosVisualizacao();
}

void specialKeys( int key, int x, int y ) {
 
  rotate_y=0; 
  rotate_x=0;
 
  //  Seta direita - aumenta rotação em 5 graus
  if (key == GLUT_KEY_RIGHT)
    rotate_y += 5;
 
  //  Seta para esquerda - diminui a rotação por 5 graus
  else if (key == GLUT_KEY_LEFT)
    rotate_y -= 5;
 
  else if (key == GLUT_KEY_UP)
    rotate_x += 5;
 
  else if (key == GLUT_KEY_DOWN)
    rotate_x -= 5;
 
  //  Requisitar atualização do display
  glutPostRedisplay();
 
}



int main(int argc, char* argv[]){
 
  //  Inicializa o GLUT e processa os parâmetros do usuário GLUT
    glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(350,300);
	glutCreateWindow("Visualizacao 3D");
	glutDisplayFunc(Desenha);
	glutReshapeFunc(AlteraTamanhoJanela);
	glutSpecialFunc(specialKeys);
	glutMainLoop();
}

