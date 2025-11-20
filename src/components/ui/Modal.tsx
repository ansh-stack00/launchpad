"use client ";

interface MyModalProps {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
}


export default function Modal({ open, onClose, children } : MyModalProps) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-md w-96 shadow-lg relative">

        <button
          className="absolute top-2 right-2 text-gray-600"
          onClick={onClose}
        >
          ✕
        </button>

        <h2 className="text-xl text-gray-900 font-bold mb-4">Details</h2>

        <div className="text-gray-800">{children}</div>
      </div>
    </div>
  );
}
