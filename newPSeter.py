import shutil
import sys

def change(num, duedate):
    # with is like your try .. finally block in this case
#    with open(str("problemSet" + num + ".tex"), 'w') as file:
        # read a list of lines into data

    #write heading
    data = ''' 
    \\documentclass{article}
    \\usepackage{graphicx} % Required for inserting images
    \\usepackage{mathrsfs}
    \\usepackage{enumerate}
    \\usepackage{enumitem}
    \\usepackage[a4paper, margin=1in]{geometry}
    \\usepackage{fancyhdr} % Required for headers and footers
    \\pagestyle{fancy}     % Activate fancy page style
    \\usepackage{amsfonts}  
    \\usepackage{amsmath}
    \\usepackage[bb=boondox]{mathalfa}
    \\newcommand{\\R}{\\mathbb{R}}
    \\newcommand{\\1}{\\mathbb{1}}
    \\newcommand{\\Q}{\\mathbb{Q}}
    \\newcommand{\\A}{\\mathscr{A}}




    \\fancyhf{}            % Clear all headers and footers
    \\fancyhead[C]{Ben Kaiser-Bulmash, Problem Set ''' + num + ''', ''' + duedate + '''}  % Add title to the center of every page

    \\title{Problem Set ''' + num + '''}
    \\author{Ben Kaiser-Bulmash}
    \\date{''' + duedate + '''}

    \\begin{document}
    \\maketitle



    \\end{document}
    '''

    # and write everything back
    with open("problemSet" + num + ".tex", 'w') as file:
        file.writelines(data) 

def copy(num, duedate):
    f = open(str("problemSet" + num + ".tex"), 'x')
    change(num, duedate)
    print("done, your prolbem set " + num + " is ready to be edited")

if __name__ == '__main__':
    num = sys.argv[1]
    duedate = sys.argv[2] + " " + sys.argv[3]
    copy(num, duedate)
