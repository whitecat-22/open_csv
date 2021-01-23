import tkinter
import tkinter.filedialog as filedialog
from tkinter import ttk
import pandas as pd


def ask_csvfile():
    path = filedialog.askopenfilename(filetypes=[('CSVファイル', '*.csv')])
    csvfile_path.set(path)


def import_csvfile():
    csvfile = csvfile_path.get()
    if not csvfile:
        return
    df = pd.read_csv(csvfile)
    print(df)


main_win = tkinter.Tk()
main_win.title("CSVファイル選択")
main_win.geometry("500x120")

main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=10, pady=10)

csvfile_label = ttk.Label(main_frm, text="CSVファイル指定")
csvfile_path = tkinter.StringVar()
csvfile_box = ttk.Entry(main_frm, textvariable=csvfile_path)
ask_btn = ttk.Button(main_frm, text="参照", command=ask_csvfile)
import_btn = ttk.Button(main_frm, text="読込", command=import_csvfile)
csvfile_label.grid(column=0, row=0, pady=10)
csvfile_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
ask_btn.grid(column=2, row=0)
import_btn.grid(column=1, row=2)

main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()
