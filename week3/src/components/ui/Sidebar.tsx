import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGauge } from "@fortawesome/free-solid-svg-icons";
import {
  faTableColumns,
  faFileLines,
  faChartPie,
  faTable,
} from "@fortawesome/free-solid-svg-icons";

export default function Sidebar() {
  return (
    <div className="h-screen w-64 bg-gradient-to-b from-slate-800 to-slate-900 shadow-xl p-4">
      
      {/* Core Section */}
      <div className="mb-6 flex flex-col">
        <h4 className="text-slate-400 text-xs uppercase tracking-wider font-semibold mb-3 px-3">
          Core
        </h4>

        <div className="mt-3 text-slate-300 px-4 py-2.5 rounded-lg cursor-pointer hover:bg-slate-700 transition-colors shadow-md font-medium flex items-center gap-3">
          <FontAwesomeIcon icon={faGauge} className="text-slate-200 text-lg" />
          <span>Dashboard</span>
        </div>
      </div>

      {/* Interface Section */}
      <div className="flex flex-col mt-6">
        <h4 className="text-slate-400 text-xs uppercase tracking-wider font-semibold mb-3 px-3">
          Interface
        </h4>

        <div className="mt-3 flex items-center gap-3 text-slate-300 px-4 py-2.5 rounded-lg cursor-pointer hover:bg-slate-700 transition-colors">
          <FontAwesomeIcon icon={faTableColumns} className="text-slate-200 text-lg" />
          <span>Layouts</span>
        </div>

        <div className="mt-3 flex items-center gap-3 text-slate-300 px-4 py-2.5 rounded-lg cursor-pointer hover:bg-slate-700 transition-colors">
          <FontAwesomeIcon icon={faFileLines} className="text-slate-200 text-lg" />
          <span>Pages</span>
        </div>
      </div>

      {/* Addons Section */}
      <div className="flex flex-col mt-6">
        <h4 className="text-slate-400 text-xs uppercase tracking-wider font-semibold mb-3 px-3">
          Addons
        </h4>

        <div className="mt-3 flex items-center gap-3 text-slate-300 px-4 py-2.5 rounded-lg cursor-pointer hover:bg-slate-700 transition-colors">
          <FontAwesomeIcon icon={faChartPie} className="text-slate-200 text-lg" />
          <span>Charts</span>
        </div>

        <div className="mt-3 flex items-center gap-3 text-slate-300 px-4 py-2.5 rounded-lg cursor-pointer hover:bg-slate-700 transition-colors">
          <FontAwesomeIcon icon={faTable} className="text-slate-200 text-lg" />
          <span>Tables</span>
        </div>
      </div>
    </div>
  );
}
