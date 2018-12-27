size=5
center=size/2

for(i=-h;i<=h;i++)
	{
		for(j=-w;j<=w;j++)
		{
			#//if((Math.abs(i)+Math.abs(j)+r)%4==0)x+="*";
			#//else x+="&nbsp;";
			x+="<span class='color"+(3-(Math.abs(i)+Math.abs(j)+r)%3)+"'>*</span>";
		}
		x+="<br />";
	}
