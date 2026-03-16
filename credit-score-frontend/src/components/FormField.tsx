interface FormFieldProps {
  label: string;
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  type?: string;
  step?: string;
  fullWidth?: boolean;
}

export default function FormField({
  label,
  value,
  onChange,
  placeholder,
  type = "text",
  step,
  fullWidth = true,
}: FormFieldProps) {
  return (
    <div className={fullWidth ? "col-span-full" : ""}>
      <label className="block text-sm font-medium text-slate-300 mb-2">{label}</label>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        step={step}
        className="w-full px-4 py-3 bg-slate-700/50 border border-slate-600 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:bg-slate-700/70 transition-all"
      />
    </div>
  );
}
