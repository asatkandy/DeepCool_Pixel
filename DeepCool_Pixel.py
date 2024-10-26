import os
import sys
import tkinter as tk
import tkinter.filedialog as fi

row_n=40
column_n=31
pixel_n=row_n*column_n
pixel_size=16
outline_size=3
box_end=pixel_size+outline_size
square_end=box_end+outline_size
selected_color='white'
case_color='white'
default_color='#333132'

widget_width=column_n*(pixel_size+2*outline_size)
widget_height=row_n*(pixel_size+2*outline_size)
window_width=round(widget_width+100)
window_height=round(widget_height+105)

pixel_color=['#FFB8CA','#CACAC8','#00A49A','#DE7C00','#FFE800','black','#FE5442','#CE70CC','white','#1295D8']
pixel_text_color=['#B8FFED','#353537','#A4000A','#0062DE','#0017FF','white','#42ECFE','#70CE72','black','#D85512']

root = tk.Tk()
root.title('DeepCool_Pixel_CH160')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_height = int(screen_height-screen_height//10)
root.geometry(f'{window_width}x{screen_height}+{(screen_width-window_width)//2}+0')
root.resizable(False,True)
root.configure(bg='#008c8c')
DCP_menu=tk.Menu(root)
root.config(menu=DCP_menu)

f0=tk.Frame(root,height=100,width=widget_width)
f1=tk.Frame(f0,height=100,width=widget_width//2)
f2=tk.Frame(f0,height=100,width=widget_width//2)
f2.grid_rowconfigure(0, weight=1)
f2.grid_columnconfigure(tuple(range(10)), weight=1)
fc1=tk.Frame(root,height=widget_height,width=widget_width)

c1=tk.Canvas(fc1,bd=0,height=widget_height,width=widget_width,cursor='hand2')
sc = tk.Scrollbar(fc1)
sc.config(command=c1.yview)
c1.config(yscrollcommand=sc.set)
c1.config(scrollregion=(0, 0, widget_width, widget_height))

f0.pack(pady=(5,0))
f1.pack(side=tk.LEFT)
f2.pack(side=tk.RIGHT)
fc1.pack(pady=(5,0))
c1.pack(side='left')
sc.pack(side='right', fill='y')


# コールバック関数をネストして定義
def callback(event):
    # print('x' + str(event.x) + 'y' + str(event.y))
    # print(color_c.get())
    # print(c1.itemcget(tagOrId=pixel_tag, option='fill'))
    pixel_tag='x' + str(int(event.x//square_end)) + 'y' + str(int(event.y//square_end))
    current_color = c1.itemcget(tagOrId=pixel_tag, option='fill')
    # print(pixel_tag)
    # print(current_color)
    if selected_color == default_color:
        c1.itemconfig(tagOrId=pixel_tag, fill=selected_color, outline=case_color)
        if not current_color == default_color:
            buttons2[pixel_color.index(current_color)].configure(text=buttons2[pixel_color.index(current_color)]['text'] - 1)
        if color_c.get():
            for k in range(0, column_n * square_end, square_end):
                for m in range(0, row_n * square_end, square_end):
                    color_c_tag = 'x' + str(k // square_end) + 'y' + str(m // square_end)
                    if not c1.itemcget(tagOrId=color_c_tag, option='fill') == default_color:
                        if c1.itemcget(tagOrId=color_c_tag, option='fill') == current_color:
                            c1.itemconfig(tagOrId=color_c_tag, fill=selected_color, outline=case_color)
                            buttons2[pixel_color.index(current_color)].configure(text=buttons2[pixel_color.index(current_color)]['text'] - 1)
    else:
        if color_c.get():
            for k in range(0, column_n * square_end, square_end):
                for m in range(0, row_n * square_end, square_end):
                    color_c_tag = 'x' + str(k // square_end) + 'y' + str(m // square_end)
                    if not c1.itemcget(tagOrId=color_c_tag,option='fill')==default_color:
                        if c1.itemcget(tagOrId=color_c_tag,option='fill')==current_color:
                            c1.itemconfig(tagOrId=color_c_tag, fill=selected_color,outline=selected_color)
                            buttons2[pixel_color.index(current_color)].configure(text=buttons2[pixel_color.index(current_color)]['text'] - 1)
                            buttons2[pixel_color.index(selected_color)].configure(text=buttons2[pixel_color.index(selected_color)]['text'] + 1)
        else:
            if c1.itemcget(tagOrId=pixel_tag, option='fill')==default_color:
                c1.itemconfig(tagOrId=pixel_tag,fill=selected_color,outline=selected_color)
                # print(pixel_color.index(selected_color))
                buttons2[pixel_color.index(selected_color)].configure(text=buttons2[pixel_color.index(selected_color)]['text']+1)
            elif c1.itemcget(tagOrId=pixel_tag, option='fill')==selected_color:
                c1.itemconfig(tagOrId=pixel_tag, fill=default_color, outline=case_color)
                buttons2[pixel_color.index(selected_color)].configure(text=buttons2[pixel_color.index(selected_color)]['text'] - 1)
            else:
                c1.itemconfig(tagOrId=pixel_tag, fill=selected_color, outline=selected_color)
                buttons2[pixel_color.index(selected_color)].configure(
                    text=buttons2[pixel_color.index(selected_color)]['text'] + 1)
                buttons2[pixel_color.index(current_color)].configure(
                    text=buttons2[pixel_color.index(current_color)]['text'] - 1)

def callback2(event):
    # sx=int(c1.winfo_rootx())+c1.winfo_width()-1
    # sy=int(c1.winfo_rooty())+c1.winfo_height()-1
    sx = c1.winfo_width()-2*outline_size
    sy = c1.winfo_height()-2*outline_size
    if sx > event.x >= 0 and sy > event.y >= 0:
        pixel_tag='x' + str(int(event.x//square_end)) + 'y' + str(int(event.y//square_end))
        current_color = c1.itemcget(tagOrId=pixel_tag, option='fill')
        if selected_color == default_color:
            if not current_color == default_color:
                c1.itemconfig(tagOrId=pixel_tag, fill=selected_color, outline=case_color)
                buttons2[pixel_color.index(current_color)].configure(text=buttons2[pixel_color.index(current_color)]['text'] - 1)
        else:
            if not c1.itemcget(tagOrId=pixel_tag, option='fill')==selected_color:
                c1.itemconfig(tagOrId=pixel_tag,fill=selected_color,outline=selected_color)
                buttons2[pixel_color.index(selected_color)].configure(text=buttons2[pixel_color.index(selected_color)]['text']+1)
                if not current_color == default_color:
                    buttons2[pixel_color.index(current_color)].configure(text=buttons2[pixel_color.index(current_color)]['text']-1)

#　ケース色の選択
def case_color_change():
    global case_color
    if Case_Button['bg'] =='white':
        case_color='black'
        case_text_color='white'
    else:
        case_color='white'
        case_text_color = 'black'

    Case_Button.configure(bg=case_color,fg=case_text_color)
    for a in range(0, column_n * square_end, square_end):
        for b in range(0, row_n * square_end, square_end):
            cc_tag = 'x' + str(a // square_end) + 'y' + str(b // square_end)
            if c1.itemcget(tagOrId=cc_tag, option='fill')==default_color:
                c1.itemconfig(tagOrId=cc_tag, outline=case_color)

# Grid Line
def grid_line():
    gl_exist=c1.find_withtag('g_line')
    if gl_exist:
        # print('exist')
        c1.delete('g_line')
    else:
        for g in range(5*square_end,column_n*square_end,5*square_end):
            c1.create_line(g, 0, g, widget_height, fill='orchid',width=2,tags='g_line')
            c1.create_text(g-15,15,fill='magenta',text=g//square_end,font=('',15),tags='g_line')
        for h in range(5*square_end,row_n*square_end,5*square_end):
            c1.create_line(0, h, widget_width, h, fill='orchid', width=2,tags='g_line')
            c1.create_text(15, h-15, fill='magenta', text=h // square_end, font=('', 15), tags='g_line')

# セーブ関数
def save_pixel():
    dataset = []
    for t in range(0, row_n * square_end, square_end):
        for s in range(0, column_n * square_end, square_end):
            data_tag='x' + str(s // square_end) + 'y' + str(t // square_end)
            dataset.append(c1.itemcget(tagOrId=data_tag, option='fill') + '\n')
    print(dataset[2])
    user_folder = os.path.expanduser('~')
    folder = os.path.join(user_folder, 'Documents')
    save_name=fi.asksaveasfilename(filetypes=[('data files','*.txt')],initialdir=folder)
    if not save_name =='':
        if not '.txt' in save_name:
            save_file=os.path.join(folder,save_name + '.txt')
        else:
            save_file=save_name
        f = open(save_file, 'w')
        f.writelines(dataset)
        f.close()

# ロード関数
def load_pixel():
    user_folder = os.path.expanduser('~')
    folder = os.path.join(user_folder, 'Documents')
    fp=fi.askopenfilename(filetypes=[('data files','*.txt')],initialdir=folder)
    if not fp=='':
        reset_pixel()
        fl=open(fp)
        dataset2=fl.readlines()
        dataset2_rs=[line.rstrip('\n') for line in dataset2]
        # print(dataset2_rs)
        v=0
        for l in dataset2_rs:
            load_tag='x' + str(v%column_n) +'y' + str(v//column_n)
            v=v+1
            if not l == default_color:
                c1.itemconfig(tagOrId=load_tag, fill=l, outline=l)
                buttons2[pixel_color.index(l)].configure(text=buttons2[pixel_color.index(l)]['text'] + 1)
                # print(load_tag)
        fl.close()


# リセット関数
def reset_pixel():
    for a in range(0, column_n * square_end, square_end):
        for b in range(0, row_n * square_end, square_end):
            reset_tag='x' + str(a // square_end) + 'y' + str(b // square_end)
            c1.itemconfig(tagOrId=reset_tag, fill=default_color, outline=case_color)
    for c in range(10):
        buttons2[c].configure(text=0)

## Pixel
for x in range(0,column_n*square_end,square_end):
    for y in range(0,row_n*square_end,square_end):
        # コールバック関数にボタン番号の値を引数で渡す
        # print(f'x{x}xo{x+box_end}y{y}yo{y+box_end}')
        c1.create_rectangle(x+outline_size//2, y+outline_size//2, x+box_end+outline_size//2, y+box_end+outline_size//2, fill=default_color,outline='white',
                            width=outline_size,outlineoffset=tk.CENTER,
                            tags='x' + str(x//square_end) + 'y' + str(y//square_end))
        c1.tag_bind('x' + str(x//square_end) + 'y' + str(y//square_end), '<Button-1>', callback)
        c1.tag_bind('x' + str(x // square_end) + 'y' + str(y // square_end), '<B1-Motion>', callback2)
        # print('x' + str(x//(box_end+outline_size)) + 'y' + str(y//(box_end+outline_size)))

# カラーセレクト関数
def color_select(event):
    print(event.widget['bg'])
    global selected_color
    selected_color = event.widget['bg']
    selected_color_text=event.widget['fg']
    Selected_Button.configure(bg=selected_color,fg=selected_color_text)

def quit_app():
    sys.exit()


## Frame1
Case_Button=tk.Button(f1,bg='white',width=4,height=2,relief='ridge',text='Case',fg='black',command=case_color_change)
Case_Button.pack(side=tk.LEFT)
Grid_line_Button=tk.Button(f1,bg='orchid',width=4,height=2,relief='ridge',text='Grid',fg='black',command=grid_line)
Grid_line_Button.pack(side=tk.LEFT)
color_c=tk.BooleanVar()
color_c.set(False)
Change_Button=tk.Checkbutton(f1,bg='yellow',width=6,height=2,relief='ridge',text='Change',fg='black',variable=color_c)
Change_Button.pack(side=tk.LEFT)
Selected_Button=tk.Button(f1,bg=selected_color,width=4,height=2,relief='flat',text='Color',fg='black')
Selected_Button.pack(side=tk.LEFT)
# Save_Button=tk.Button(f1,bg='yellow',width=4,height=2,relief='ridge',text='Save',command=save_pixel)
# Save_Button.pack(side=tk.LEFT)
# Load_Button=tk.Button(f1,bg='green',width=4,height=2,relief='ridge',text='Load',command=load_pixel)
# Load_Button.pack(side=tk.LEFT)
# Reset_Button=tk.Button(f1,bg=default_color,width=4,height=2,relief='ridge',text='Reset',command=reset_pixel)
# Reset_Button.pack(side=tk.RIGHT)

## Frame 2
buttons2 =[]
for j in range(10):
    buttons2.append(tk.Button(f2, bg=pixel_color[j],width=4,height=2,relief='ridge',text=0,fg=pixel_text_color[j]))
    buttons2[j].grid(row=0,column=j)
    buttons2[j].bind('<1>',color_select)
default_button=tk.Button(f2, bg=default_color,width=4,height=2,relief='ridge',text='hole',fg='white')
default_button.grid(row=0,column=11)
default_button.bind('<1>',color_select)

# Menu
menu_font=('',10)
file_menu=tk.Menu(DCP_menu,tearoff=False,font=menu_font)
file_menu.add_command(label='Save as txt',command=save_pixel)
file_menu.add_command(label='Load',command=load_pixel)
reset_menu=tk.Menu(DCP_menu,tearoff=False,font=menu_font)
reset_menu.add_command(label='Reset',command=reset_pixel)
exit_menu=tk.Menu(DCP_menu,tearoff=False,font=menu_font)
exit_menu.add_command(label='Exit',command=quit_app)

DCP_menu.add_cascade(label='File',menu=file_menu)
DCP_menu.add_cascade(label='Reset',menu=reset_menu)
DCP_menu.add_cascade(label='Exit',menu=exit_menu)

root.mainloop()
