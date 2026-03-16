import { useEffect, useRef, useState } from "react";
import { ChevronDown } from "lucide-react";

interface Option {
  value: string;
  label: string;
}

interface FormSelectProps {
  label: string;
  value: string;
  onChange: (value: string) => void;
  options: (string | Option)[];
  fullWidth?: boolean;
  placeholder?: string;
}

export default function FormSelect({
  label,
  value,
  onChange,
  options,
  fullWidth = true,
  placeholder = "Selecione uma opção",
}: FormSelectProps) {
  const [open, setOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const normalizedOptions: Option[] = options.map((option) =>
    typeof option === "object"
      ? option
      : { value: option, label: option }
  );

  const selectedOption = normalizedOptions.find((opt) => opt.value === value);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target as Node)
      ) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleSelect = (optionValue: string) => {
    onChange(optionValue);
    setOpen(false);
  };

  return (
    <div className={fullWidth ? "col-span-full" : ""}>
      <label className="block text-sm font-medium text-slate-300 mb-2">
        {label}
      </label>

      <div className="relative" ref={containerRef}>
        <button
          type="button"
          onClick={() => setOpen((prev) => !prev)}
          className="w-full px-4 py-3 bg-slate-700/50 border border-slate-600 rounded-lg text-white focus:outline-none focus:border-blue-500 focus:bg-slate-700/70 transition-all flex items-center justify-between"
        >
          <span className={selectedOption ? "text-white" : "text-slate-500"}>
            {selectedOption ? selectedOption.label : placeholder}
          </span>
          <ChevronDown
            className={`w-5 h-5 text-slate-400 transition-transform ${
              open ? "rotate-180" : ""
            }`}
          />
        </button>

        {open && (
          <div className="absolute z-50 mt-2 w-full rounded-lg border border-slate-600 bg-slate-800 shadow-lg max-h-60 overflow-y-auto">
            {normalizedOptions.map((option) => (
              <button
                key={option.value}
                type="button"
                onClick={() => handleSelect(option.value)}
                className={`w-full text-left px-4 py-3 transition-colors hover:bg-slate-700 ${
                  option.value === value
                    ? "bg-slate-700 text-blue-400"
                    : "text-white"
                }`}
              >
                {option.label}
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}