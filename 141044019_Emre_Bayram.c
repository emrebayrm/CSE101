#include <stdio.h>

/*######################################*
 * Name : Emre                          *
 * Surname : Bayram                     *
 * NO : 141044019                       *
 *######################################*/

void drawerMenu(void);
void rhomboidDrawer(void);
void traingleDrawer(void);
void circleDrawer(void);

int main()
{
    int user_choise;
    while (1)
    {
		drawerMenu();
		printf("->");
		scanf("%d",&user_choise);

		if (user_choise ==1)
			traingleDrawer();

		else if (user_choise ==2)
			rhomboidDrawer();

		else if(user_choise ==3)
			circleDrawer();

		else if (user_choise ==4)
			break;
		else
			printf ("invalid input,please try again!");
    }
    return 0;
}

void drawerMenu(void)
{
    printf("\nWelcome To Drawer's Home!\n");
	printf("[1] Triangle\n");
	printf("[2] Rhomboid\n");
	printf("[3] Circle\n");
	printf("[4] Exit\n");
	printf("Select a Shape:\n");
}

void rhomboidDrawer(void)
{
    int i,j;
    int w,h;
    int x;

    printf("Enter w side size-> ");
    scanf("%d",&w);
    printf("Enter h side size-> ");
    scanf("%d",&h);

    for(i = 0; i < h; ++i)
    {
        j =0;
        for(x = 0 ; x < i ; ++x )
            printf(" ");
        for(j = 0; j < w ; ++j )
            printf("* ");
        printf("\n");
    }
}

void traingleDrawer(void)
{
    int h ;
    int i = 1 ,k = 0;
    int space;

    printf("Enter height of triangle -> ");
    scanf("%d",&h);

    while(i <= h)
    {
        space = 1;

        while(space <= h - i )
        {
            printf(" ");

            space++;
        }
        while( k !=2*i - 1)
        {
            printf("*");
            ++k;
        }
        k = 0;

        ++i;
        printf("\n");
    }
}

void circleDrawer(void)
{
    int r;
    double y;
    double x;
    double value;
    double r_out;

    printf("Enter Radius ->");
    scanf("%d",&r);

    r_out = r + 0.4;
    y = r;

    while( y >= -r)
    {
        x = -r;
        while(x <r_out)
        {
            value = x*x + y*y;
            if(value <= r_out * r_out)
                printf("*");
            else printf(" ");

            x += 0.5;
        }
        printf("\n");

        y -= 1;
    }

}
