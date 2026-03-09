# Case Study: Arjun and the Archivist’s Rules

# Arjun was an apprentice archivist in the City of Timelines, a place where knowledge was preserved under strict rules.
# Every object stored in the archive followed a data discipline; nothing was random, and nothing was accidental.

# One afternoon, the Chief Archivist handed Arjun two enchanted records.

# “These are not just containers,” she said.
# “They decide how information behaves.”

# -------------------------------------------------------------------------------------------------------------------------

# Record One: The Chronicle Scroll

# The first record was called the Chronicle Scroll.
# “This scroll preserves history exactly as it is written,” said the Archivist.
# “Once sealed, its contents can never be altered.”
# The Archivist explained that the Chronicle Scroll works like a Tuple.
# Chronicle Scroll = Tuple

# Arjun recorded the sequence of royal events:
# chronicle = ("Coronation", "War Declared", "Peace Treaty")

# He reviewed the entries:
# print(chronicle[1])
# Output:
# War Declared

# Encouraged, Arjun tried to revise history:
# chronicle[1] = "Secret Negotiation"
# The archive rejected the change immediately.

# What Arjun Observed
# Events stayed in the same order
# Each event had a fixed position
# Once recorded, entries could not be changed
# The scroll allowed repeated events if history demanded it
# Inference:
# Tuples preserve order, are immutable, and can store duplicates.
# They use round brackets ().

# ------------------------------------------------------------------------------------------------------------------------

# Record Two: The Artifact Vault

# The second record was called the Artifact Vault.
# “This vault only cares about what exists, not how it is arranged,” said the Archivist.
# “And it never keeps the same artifact twice.”
# The vault behaves like a Set.
# Artifact Vault = Set

# Arjun logged collected artifacts:
# artifacts = {"ring", "amulet", "ring", "scroll"}

# When he checked the vault, he saw:
# print(artifacts)
# Output (order may vary):
# {'ring', 'amulet', 'scroll'}
# The duplicate artifact had vanished.

# Managing the Artifact Vault
# Unlike the Chronicle Scroll, the vault was flexible.
# Arjun added a new artifact:
# artifacts.add("crystal")
# Later, he removed one:
# artifacts.remove("ring")
# The vault updated instantly.

# What Arjun Observed 
# Order was unpredictable
# Duplicate artifacts were automatically ignored 
# Items could be added or removed freely
# The vault focused only on uniqueness

# Inference:
# Sets are unordered, mutable, and store only unique elements.
# They use curly brackets {}.

# --------------------------------------------------------------------------------------------------------------------

# Arjun attempted to change an entry inside the Chronicle Scroll using:
# chronicle[1] = "Secret Negotiation"
# Why did this action fail?
#  Because tuples do not support indexing
#  Because the element did not exist
#  Because the Chronicle Scroll preserves order only
#  Because the Chronicle Scroll is immutable   (Right Answer)


# When Arjun created the Artifact Vault as:
# artifacts = {"ring", "amulet", "ring", "scroll"}
# Why did the final vault contain fewer items than expected?
#  Because sets automatically sort items
#  Because duplicate elements are ignored    (Right Answer)
#  Because only strings are allowed
#  Because indexing is not supported


# Which operation was possible on the Artifact Vault but impossible on the Chronicle Scroll?
#  Accessing an element using index
#  Preserving insertion order
#  Modifying the container after creation    (Right Answer)
#  Allowing duplicate values


# Arjun noticed that printing the Artifact Vault showed items in an unpredictable order. What caused this behavior?
#  The vault was empty initially
#  Python randomly shuffles set elements
#  Sets do not maintain insertion order    (Right Answer)
#  Duplicate elements change ordering


# Which of the following would raise an error if attempted on the Chronicle Scroll?
#  Checking length
#  Accessing an element
#  Iterating through elements
#  Updating an existing element    (Right Answer)


# Why was the Artifact Vault more suitable for tracking collected artifacts?
#  It supports indexing
#  It allows duplicates
#  It guarantees uniqueness    (Right Answer)
#  It preserves historical order


# If Arjun needed to ensure that historical records could never be altered, which structure was most appropriate?
#  List
#  Set
#  Dictionary
#  Tuple    (Right Answer)


# Which statement about indexing is TRUE based on the case study?
#  Both tuples and sets support indexing
#  Only sets support indexing
#  Only tuples support indexing    (Right Answer)
#  Neither supports indexing


# Arjun removed an item from the Artifact Vault successfully. Why was this operation safe?
#  Because sets allow modification    (Right Answer)
#  Because tuples allow removal
#  Because removal works only on strings
#  Because indexing was used


# Which inference correctly matches both records used by Arjun?
#  Chronicle Scroll → unordered, mutable
#  Artifact Vault → ordered, immutable
#  Chronicle Scroll → ordered, immutable    (Right Answer)
#  Artifact Vault → ordered, duplicate-allowed