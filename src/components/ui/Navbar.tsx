import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";

export default function Navbar() {
   return (
    <>
        <header className="flex justify-between items-center w-full h-20 bg-gradient-to-r from-slate-900 to-slate-800 shadow-lg px-6">
            <div className="box1 bg-gradient-to-r from-blue-600 to-blue-500 px-5 py-2 rounded-lg flex items-center justify-between gap-40 hover:shadow-md transition-shadow"> 
                <h1 className="text-white font-semibold text-lg">Start BootStrap</h1>
                <FontAwesomeIcon icon={faBars} className="text-white text-lg cursor-pointer hover:opacity-80 transition-opacity" />
            </div>
            <div className="box2 h-10 flex items-center gap-4" >
                <div className="bg-slate-700 rounded-lg px-4 py-2 flex items-center gap-2 shadow-md hover:bg-slate-600 transition-colors">
                    <input type="text" 
                        className="outline-none border-none bg-transparent text-white placeholder-slate-400 w-48"
                        placeholder="Search..."/>
                    <FontAwesomeIcon icon={faMagnifyingGlass} className="text-slate-300 text-sm" />
                </div>
                <div className="bg-slate-700 rounded-full w-10 h-10 flex items-center justify-center hover:bg-slate-600 transition-colors cursor-pointer shadow-md">
                    <FontAwesomeIcon icon={faUser} className="text-slate-200 text-lg" />
                </div>
            </div>
        </header>
    </>
   )
}