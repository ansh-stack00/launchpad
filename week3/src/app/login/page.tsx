import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { 
    faUser, 
    faLock 
} from "@fortawesome/free-solid-svg-icons";


export default function LoginPage() {
  return (
    <div className="h-full w-full flex justify-center items-center bg-gray-100">
      <div className="w-[50%] h-[60%]  p-6 rounded-lg shadow-lg space-y-5 ">
        <div className="flex justify-between">
            <h1 className="text-gray-500 text-2xl  ">Sign to continue.</h1>
        </div>
        <div className="flex items-center gap-3 p-2 bg-gray-200 rounded-md mt-10">
          <FontAwesomeIcon icon={faUser} className="text-gray-600" />
          <input
            type="text"
            placeholder="Username"
            className="bg-transparent outline-none w-full"
          />
        </div>

        <div className="flex items-center gap-3 p-2 bg-gray-200 rounded-md">
          <FontAwesomeIcon icon={faLock} className="text-gray-600" />
          <input
            type="password"
            placeholder="Password"
            className="bg-transparent outline-none w-full"
          />
        </div>

        <div className="flex justify-between items-center text-sm mt-7">
          <label className="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" className="text-gray-600" />
            <span>Remember me</span>
          </label>

          <button className="text-blue-600 hover:underline">
            Forgot Password?
          </button>
        </div>

      
        <button className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition mt-3.5">
          Login
        </button>
      </div>
    </div>
  );
}
