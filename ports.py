import mido
import rtmidi

out = rtmidi.MidiOut()
ports_dict = {k:v for (v,k) in enumerate(out.get_ports())}
print(ports_dict)

mido.set_backend('mido.backends.rtmidi')

print(mido.get_input_names())
print(mido.get_output_names())
